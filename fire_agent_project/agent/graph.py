"""LangGraph 기반 메인 실행 흐름. 패키지가 없는 개발 환경은 순차 fallback."""
from agent.nodes import analyze_intent, create_plan, execute_tools, replan_if_needed, assess_constraints, generate_answer
from agent.events import publish


def _stage(name, fn):
    def wrapped(state):
        sid=state.get('session_id','local-session')
        publish(sid,'stage_started',stage=name)
        result=fn(state)
        publish(sid,'stage_finished',stage=name,summary={k:(len(v) if isinstance(v,(list,dict)) else v) for k,v in result.items()})
        return result
    return wrapped

try:
    from langgraph.graph import StateGraph, END
    from agent.state import AgentState
    builder=StateGraph(AgentState)
    builder.add_node('analyze',_stage('요청 분석',analyze_intent))
    builder.add_node('plan',_stage('작업 계획 수립',create_plan))
    builder.add_node('execute',_stage('Tool 실행 및 결과 통합',execute_tools))
    builder.add_node('replan',_stage('재계획',replan_if_needed))
    def judge(state):
        sid=state.get('session_id','local-session'); publish(sid,'stage_started',stage='제약 적합성 판단')
        result=assess_constraints(state); publish(sid,'judgement',constraints_satisfied=result['constraints_satisfied'],evidence=result['evidence'])
        publish(sid,'stage_finished',stage='제약 적합성 판단')
        return {'assessment':result,'constraints_satisfied':result['constraints_satisfied']}
    def answer(state):
        sid=state.get('session_id','local-session'); publish(sid,'stage_started',stage='최종 응답 생성')
        result={'final_answer':generate_answer(state,state.get('assessment',{}))}
        publish(sid,'stage_finished',stage='최종 응답 생성')
        return result
    builder.add_node('judge',judge); builder.add_node('answer',answer)
    builder.set_entry_point('analyze'); builder.add_edge('analyze','plan'); builder.add_edge('plan','execute'); builder.add_edge('execute','replan'); builder.add_edge('replan','judge'); builder.add_edge('judge','answer'); builder.add_edge('answer',END)
    graph=builder.compile()
except Exception:
    graph=None


def run_agent(user_request, session_id='local-session', memory=None):
    state={'user_request':user_request,'session_id':session_id,'retry_count':0,'max_retries':2,'execution_logs':[],'tool_results':{},'memory':memory or []}
    publish(session_id,'run_started',user_request=user_request)
    if graph is not None:
        result=graph.invoke(state)
    else:
        for name,fn in [('요청 분석',analyze_intent),('작업 계획 수립',create_plan),('Tool 실행 및 결과 통합',execute_tools),('재계획',replan_if_needed)]:
            publish(session_id,'stage_started',stage=name); state.update(fn(state)); publish(session_id,'stage_finished',stage=name)
        publish(session_id,'stage_started',stage='제약 적합성 판단')
        assessment=assess_constraints(state); state['assessment']=assessment; state['constraints_satisfied']=assessment['constraints_satisfied']
        publish(session_id,'judgement',constraints_satisfied=assessment['constraints_satisfied'],evidence=assessment['evidence'])
        publish(session_id,'stage_finished',stage='제약 적합성 판단')
        publish(session_id,'stage_started',stage='최종 응답 생성')
        state['final_answer']=generate_answer(state,assessment)
        publish(session_id,'stage_finished',stage='최종 응답 생성')
        result=state
    publish(session_id,'run_finished',selected_tools=result.get('selected_tools',[]),retry_count=result.get('retry_count',0))
    return result
