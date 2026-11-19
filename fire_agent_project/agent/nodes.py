"""산불 위험 분석 Agent 노드. API가 확인하지 못한 값은 추정하지 않는다."""
import re
from datetime import date, timedelta
from tools import TOOLS
from agent.events import publish
from agent import llm

REGIONS = {
 '전국': None, '서울': '11', '부산': '26', '대구': '27', '인천': '28', '광주': '29',
 '대전': '30', '울산': '31', '세종': '36', '경기도': '41', '충청북도': '43',
 '충청남도': '44', '전라북도': '45', '전라남도': '46', '경상북도': '47',
 '경상남도': '48', '제주도': '50', '강원도': '51', '강원특별자치도': '51'
}
REGION_ALIASES = {'강원':'강원도','경기':'경기도','충북':'충청북도','충남':'충청남도','전북':'전라북도','전남':'전라남도','경북':'경상북도','경남':'경상남도','제주':'제주도'}
WEATHER_STATIONS = {
 '강원도':['90','101','105','106','114','121','211','216'],
 '서울':['108'], '경기도':['119','112'], '충청북도':['131'], '충청남도':['133'],
 '전라북도':['146'], '전라남도':['156'], '경상북도':['143'], '경상남도':['155'], '부산':['159'], '제주도':['184']
}


def _analyze_intent_rules(state):
    req=state['user_request']
    # 후속 요청에서 지역/조건을 생략한 경우 직전 사용자 요청을 문맥으로 활용
    memory=state.get('memory',[])
    followup=any(w in req for w in ['그럼','그 지역','같은 조건','아까','방금','거기','추가로','그중'])
    previous=next((m.get('content','') for m in reversed(memory) if m.get('role')=='user'), '')
    parse_req=(previous+' '+req) if followup and previous else req
    region='전국'
    region_text=req
    for alias, canonical in REGION_ALIASES.items():
        if alias in region_text: region=canonical; break
    if region=='전국':
        for name in sorted(REGIONS, key=len, reverse=True):
            if name!='전국' and name in region_text: region=name; break
    if region=='전국' and followup:
        for alias, canonical in REGION_ALIASES.items():
            if alias in previous: region=canonical; break
        if region=='전국':
            for name in sorted(REGIONS, key=len, reverse=True):
                if name!='전국' and name in previous: region=name; break
    m=re.search(r'(\d+)\s*(?:곳|개|지역)',req) or re.search(r'(\d+)\s*(?:곳|개|지역)',parse_req)
    count=max(1,min(int(m.group(1)),50)) if m else 5
    chat_only=any(w in req.lower() for w in ['안녕','반가워','고마워','감사','사용법','무엇을 할 수','도움말'])
    include_risk=not chat_only and any(w in parse_req for w in ['위험','위험도','예보','고위험','예측','추천','산불'])
    include_history=not chat_only and any(w in parse_req for w in ['과거','이력','발생 기록','발생 현황','산불 발생'])
    include_weather=not chat_only and any(w in parse_req for w in ['기상','날씨','습도','기온','강수량','풍속','건조'])
    include_detail=not chat_only and any(w in req for w in ['상세','자세히','세부 정보'])
    if not chat_only and not any([include_risk,include_history,include_weather]): include_risk=True
    # 명시된 날짜가 있으면 YYYYMMDD 또는 YYYY-MM-DD를 인식. 미지정 시 최근 30일.
    dates=re.findall(r'(20\d{2})[-./]?(\d{2})[-./]?(\d{2})',req)
    if not dates and followup: dates=re.findall(r'(20\d{2})[-./]?(\d{2})[-./]?(\d{2})',previous)
    if len(dates)>=2:
        start=''.join(dates[0]); end=''.join(dates[1])
    else:
        end=(date.today()-timedelta(days=1)); start=end-timedelta(days=29)
        start=start.strftime('%Y%m%d'); end=end.strftime('%Y%m%d')
    return {'intent':{'region':region,'region_code':REGIONS.get(region),'count':count,'include_risk':include_risk,
      'include_history':include_history,'include_weather':include_weather,'include_detail':include_detail,'start_date':start,'end_date':end,
      'analyzed_at':date.today().isoformat(),'request_type':'chat' if chat_only else 'analysis'}}


def analyze_intent(state):
    """LLM으로 요청 조건을 추출하고, 실패/미설정 시 기존 규칙 분석으로 대체한다."""
    baseline = _analyze_intent_rules(state)
    intent = dict(baseline['intent'])
    sid = state.get('session_id', 'local-session')
    req = state.get('user_request', '')
    if intent.get('request_type') == 'chat':
        status = {'used': False, 'source': 'rules', 'reason': '일반 대화이므로 Tool/LLM 호출 생략'}
        publish(sid, 'llm_decision', **status, decision='chat')
        return {'intent': intent, 'llm_status': status}

    memory = state.get('memory', [])
    context = '\n'.join(
        f"{m.get('role', 'unknown')}: {m.get('content', '')}"
        for m in memory[-6:] if isinstance(m, dict)
    )
    try:
        parsed = llm.analyze_request(req, context)
        if hasattr(parsed, 'model_dump'):
            parsed = parsed.model_dump()
        if not isinstance(parsed, dict):
            raise ValueError('LLM 응답 형식이 올바르지 않습니다.')

        region = str(parsed.get('region') or intent['region']).strip()
        region = REGION_ALIASES.get(region, region)
        if region not in REGIONS:
            region = intent['region']
        # 모델이 지역을 놓치고 기본값(전국)을 반환하면 규칙 분석에서 확인한 지역을 보존한다.
        if region == '전국' and intent['region'] != '전국' and '전국' not in req:
            region = intent['region']
        count = parsed.get('count', intent['count'])
        # 명시적 개수를 규칙 분석이 이미 찾았는데 모델이 기본값 5를 반환한 경우 보존한다.
        if count == 5 and intent['count'] != 5:
            count = intent['count']
        try:
            count = max(1, min(int(count), 50))
        except (TypeError, ValueError):
            count = intent['count']

        for key in ('include_risk', 'include_history', 'include_weather', 'include_detail'):
            if isinstance(parsed.get(key), bool):
                intent[key] = parsed[key]
        if not any(intent[k] for k in ('include_risk', 'include_history', 'include_weather')):
            intent['include_risk'] = True
        request_type = parsed.get('request_type')
        if request_type in ('chat', 'analysis'):
            intent['request_type'] = request_type
        if intent['request_type'] == 'chat':
            for key in ('include_risk', 'include_history', 'include_weather', 'include_detail'):
                intent[key] = False
        intent['region'] = region
        intent['region_code'] = REGIONS.get(region)
        intent['count'] = count

        for key in ('start_date', 'end_date'):
            value = parsed.get(key)
            if isinstance(value, str):
                digits = re.sub(r'[^0-9]', '', value)
                if len(digits) == 8 and digits.startswith('20'):
                    intent[key] = digits
        if intent['start_date'] > intent['end_date']:
            intent['start_date'], intent['end_date'] = intent['end_date'], intent['start_date']

        status = {'used': True, 'source': 'openai', 'model': llm.configured_model(),
                  'reason': str(parsed.get('reasoning') or 'LLM이 사용자 요청에서 조회 조건을 추출했습니다.')}
        publish(sid, 'llm_decision', **status, decision={k: intent[k] for k in (
            'region', 'count', 'include_risk', 'include_history', 'include_weather', 'include_detail',
            'start_date', 'end_date', 'request_type')})
    except Exception as exc:
        # 키 미설정/네트워크/모델 오류를 사용자 요청 실패로 전파하지 않는다.
        reason = str(exc) if str(exc) == 'OPENAI_API_KEY_NOT_CONFIGURED' else 'LLM 호출에 실패하여 규칙 기반 분석을 사용했습니다.'
        status = {'used': False, 'source': 'rules_fallback', 'reason': reason}
        publish(sid, 'llm_decision', **status, decision={k: intent[k] for k in (
            'region', 'count', 'include_risk', 'include_history', 'include_weather', 'include_detail')})
    return {'intent': intent, 'llm_status': status}


def create_plan(state):
    i=state['intent']; region=i['region']; plan=[]; selected=[]
    if i['include_risk']:
        args={'sido_code':i['region_code']} if i['region_code'] else {}
        plan.append({'tool':'search_fire_risk','purpose':f'{region} 산불 위험예보 후보 조회','arguments':args,'region_filter':region,'needs':[]}); selected.append('search_fire_risk')
        if i.get('include_detail'):
            plan.append({'tool':'search_fire_risk_detail','purpose':'후보 지역의 시군구별 산불위험예보 상세 확인','arguments':{},'dynamic_from':'search_fire_risk','needs':[]}); selected.append('search_fire_risk_detail')
    if i['include_history']:
        plan.append({'tool':'search_fire_history','purpose':f'{region} 과거 산불 발생 기록 조회','arguments':{'start_date':i['start_date'],'end_date':i['end_date']},'region_filter':region,'needs':[]}); selected.append('search_fire_history')
    if i['include_weather']:
        stations=WEATHER_STATIONS.get(region, WEATHER_STATIONS['강원도'] if region=='전국' else ['108'])
        plan.append({'tool':'search_weather','purpose':f'{region} 기상 관측자료 조회','arguments':{'start_date':i['start_date'],'end_date':i['end_date'],'stations':stations},'region_filter':region,'needs':[]}); selected.append('search_weather')
    return {'plan':plan,'selected_tools':selected}


def _region_match(item, region):
    if region=='전국': return True
    text=' '.join(str(v) for v in item.values())
    aliases=[region, region.replace('특별자치도',''), region.replace('도','')]
    return any(a and a in text for a in aliases)


def execute_tools(state):
    sid=state.get('session_id','local-session'); results={}; logs=[]
    for step in state.get('plan',[]):
        name=step['tool']; args=step.get('arguments',{}); tool=TOOLS.get(name)
        publish(sid,'tool_call_started',tool=name,arguments=args)
        if tool is None:
            result={'ok':False,'error':{'code':'UNKNOWN_TOOL','message':'등록되지 않은 Tool입니다.'}}
        elif step.get('dynamic_from') == 'search_fire_risk':
            source=results.get('search_fire_risk',{})
            source_items=source.get('data',{}).get('items',[]) if source.get('ok') else []
            details=[]
            for candidate in source_items[:5]:
                code=candidate.get('sigucode') or candidate.get('regioncode')
                if code and str(code).isdigit() and len(str(code))==5:
                    detail=tool.run(sigungu_code=str(code))
                    details.append({'sigungu_code':str(code),'result':detail})
            result={'ok':bool(details),'data':{'count':len(details),'items':details}} if details else {'ok':False,'error':{'code':'NO_DETAIL_KEY','message':'후보 응답에서 상세 조회용 시군구 코드를 찾지 못했습니다.'}}
        else:
            result=tool.run(**args)
        if result.get('ok') and step.get('region_filter') not in (None,'전국'):
            data=result.get('data',{}); items=data.get('items',[]) if isinstance(data,dict) else []
            if name in ('search_fire_risk','search_fire_history'):
                filtered=[x for x in items if _region_match(x,step['region_filter'])]
                data={**data,'items':filtered,'count':len(filtered),'region_filter_applied':True}
                result={'ok':True,'data':data} if filtered else {'ok':False,'error':{'code':'NO_REGION_DATA','message':f"{step['region_filter']}에 해당하는 결과가 없습니다."},'data':{**data,'items':[],'count':0}}
        results[name]=result
        status='SUCCESS' if result.get('ok') else 'FAILED'
        entry={'tool':name,'status':status,'arguments':args,'result_summary':({'count':result.get('data',{}).get('count')} if result.get('ok') else result.get('error'))}
        logs.append(entry)
        publish(sid,'tool_call_finished',tool=name,status=status,arguments=args,result_summary=entry['result_summary'])
    return {'tool_results':results,'execution_logs':logs}



def replan_if_needed(state):
    """지역 필터/조회 결과가 비어 있으면 위험예보 후보만 전국 조회로 한 번 보완한다."""
    risk=state.get('tool_results',{}).get('search_fire_risk',{})
    if not state.get('intent',{}).get('include_risk') or risk.get('ok'):
        return {}
    if state.get('retry_count',0) >= state.get('max_retries',2):
        return {}
    code=risk.get('error',{}).get('code')
    if code not in ('NO_DATA','NO_REGION_DATA','UPSTREAM_ERROR'):
        return {}
    sid=state.get('session_id','local-session')
    publish(sid,'replan_started',reason=code,attempt=state.get('retry_count',0)+1,detail='지역 조건 조회 실패로 전국 후보 조회 후 지역을 재필터링')
    result=TOOLS['search_fire_risk'].run()
    state['retry_count']=state.get('retry_count',0)+1
    if result.get('ok') and state['intent']['region']!='전국':
        region=state['intent']['region']
        filtered=[x for x in result['data'].get('items',[]) if _region_match(x,region)]
        if filtered:
            result={'ok':True,'data':{**result['data'],'items':filtered,'count':len(filtered),'region_filter_applied':True,'retrieved_by':'nationwide_fallback'}}
        else:
            result={'ok':False,'error':{'code':'NO_REGION_DATA','message':f'{region} 후보를 전국 조회에서도 찾지 못했습니다.'}}
    state.setdefault('tool_results',{})['search_fire_risk']=result
    log={'tool':'search_fire_risk','status':'SUCCESS' if result.get('ok') else 'FAILED','arguments':{},'replan':True,'result_summary':result.get('data',{}).get('count') if result.get('ok') else result.get('error')}
    state.setdefault('execution_logs',[]).append(log)
    publish(sid,'tool_call_finished',tool='search_fire_risk',status=log['status'],arguments={},replan=True,result_summary=log['result_summary'])
    publish(sid,'replan_finished',success=result.get('ok'),attempt=state['retry_count'])
    return {'tool_results':state['tool_results'],'execution_logs':state['execution_logs'],'retry_count':state['retry_count']}


def assess_constraints(state):
    results=state.get('tool_results',{}); candidates=[]; evidence=[]
    risk=results.get('search_fire_risk',{})
    if risk.get('ok'):
        for item in risk['data'].get('items',[]):
            candidates.append({'name':item.get('sigun') or item.get('doname') or item.get('regioncode') or '지역명 미확인',
              'region':item.get('doname'),'risk_index':item.get('maxi'),'risk_mean':item.get('meanavg'),
              'risk_min':item.get('mini'),'forecast':{k:item.get(k) for k in ['d1','d2','d3','d4'] if k in item},'source':'산불위험예보 API','raw':item})
        evidence.append(f"산불위험예보 API에서 {len(candidates)}건 확인")
    history=results.get('search_fire_history',{})
    if history.get('ok'): evidence.append(f"과거 산불 기록 {history['data'].get('count',0)}건 조회")
    weather=results.get('search_weather',{})
    if weather.get('ok'): evidence.append(f"기상 관측자료 {weather['data'].get('count',0)}건 조회")
    # 외부 API는 산불 발생 확률을 제공하지 않으므로 확률/위험등급을 임의 산출하지 않는다.
    candidates.sort(key=lambda x: (float(x['risk_index']) if str(x.get('risk_index','')).replace('.','',1).isdigit() else -1),reverse=True)
    selected=candidates[:state.get('intent',{}).get('count',5)]
    return {'candidates':selected,'constraints_satisfied':bool(selected) if risk.get('ok') else None,
      'evidence':evidence,'history':history.get('data',{}).get('items',[]) if history.get('ok') else [],
      'weather':weather.get('data',{}).get('items',[]) if weather.get('ok') else []}



def generate_answer(state, assessment):
    intent = state.get('intent') or {}
    assessment = assessment if isinstance(assessment, dict) else {}

    candidates = assessment.get('candidates') or []
    evidence = assessment.get('evidence') or []
    history = assessment.get('history') or []
    weather = assessment.get('weather') or []

    if intent.get('request_type') == 'chat':
        return (
            '안녕하세요. 산불위험예보, 과거 산불 발생 기록, '
            '기상 관측자료를 조회하고 결과와 근거를 정리할 수 있습니다. '
            '지역과 확인하고 싶은 정보를 말씀해 주세요.'
        )

    region = intent.get('region') or '요청 지역'
    lines = [f"## {region} 산불 위험 정보 조회 결과", '']

    if intent.get('include_risk'):
        if candidates:
            lines.append('### 산불위험예보 후보')
            for n, c in enumerate(candidates, 1):
                lines.append(
                    f"{n}. **{c.get('name', '지역명 미확인')}** — "
                    f"위험예보 지수(maxi): "
                    f"{c.get('risk_index') if c.get('risk_index') is not None else '자료 없음'}; "
                    f"평균값: "
                    f"{c.get('risk_mean') if c.get('risk_mean') is not None else '자료 없음'}"
                )
            lines.append('')
        else:
            lines.append(
                '산불위험예보 후보를 확보하지 못했습니다. '
                '지역 코드, API 응답 또는 Agent의 데이터 전달 과정을 확인해야 합니다.'
            )

    if evidence:
        lines.append('### 함께 조회한 근거')
        lines.extend(f'- {item}' for item in evidence)

    if intent.get('include_history') and history:
        lines.append('### 과거 산불 기록 예시')
        for item in history[:5]:
            lines.append(
                f"- {item.get('year', '')}년 {item.get('month', '')}월 "
                f"{item.get('day', '')}일 · {item.get('sido', '')} "
                f"{item.get('sigungu', '')} · 원인: "
                f"{item.get('cause') or '자료 없음'} · 피해면적: "
                f"{item.get('damage_area') or '자료 없음'}"
            )

    if intent.get('include_weather') and weather:
        lines.append('### 기상 관측자료 예시')
        for item in weather[:5]:
            lines.append(
                f"- {item.get('date', '')} · 관측소 "
                f"{item.get('station_name', item.get('station', ''))} · "
                f"평균기온 {item.get('avg_temperature', '자료 없음')} · "
                f"평균습도 {item.get('avg_humidity', '자료 없음')} · "
                f"강수량 {item.get('daily_rainfall', '자료 없음')} · "
                f"평균풍속 {item.get('avg_wind_speed', '자료 없음')}"
            )

    errors = [
        f"{name}: {result.get('error', {}).get('message', '조회 실패')}"
        for name, result in state.get('tool_results', {}).items()
        if isinstance(result, dict) and not result.get('ok')
    ]

    if errors:
        lines.extend(['', '### 조회 실패 또는 제한사항'])
        lines.extend(f'- {error}' for error in errors)

    if not assessment:
        lines.extend([
            '',
            '### 데이터 처리 안내',
            '- Agent의 평가 결과가 전달되지 않았습니다.',
            '- 실행 그래프의 assessment 상태 전달을 확인해야 합니다.'
        ])

    lines.extend([
        '',
        '### 해석 시 주의사항',
        '- 위험예보 지수는 API 원자료이며 산불 발생 확률이 아닙니다.',
        '- 기상 관측값과 과거 발생 기록은 참고자료입니다.',
        '- 산불 위험은 급변할 수 있으므로 공식 당국의 최신 안내를 우선 확인하세요.'
    ])

    return '\n'.join(lines)
