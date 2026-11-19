"""외부 API 키 없이 실행 가능한 핵심 구조 테스트."""
import unittest
from unittest.mock import patch
from agent.nodes import analyze_intent, create_plan, execute_tools, assess_constraints, generate_answer
from agent.graph import run_agent
from tools import TOOLS, ok
import storage

class ProjectTests(unittest.TestCase):
    def test_intent_region_and_flags(self):
        s={'user_request':'강원도 산불 위험 지역 3곳과 기상 자료를 확인해줘','memory':[]}
        out=analyze_intent(s)['intent']
        self.assertEqual(out['region'],'강원도'); self.assertEqual(out['region_code'],'51')
        self.assertEqual(out['count'],3); self.assertTrue(out['include_weather'])

    def test_llm_intent_is_validated_and_used(self):
        from unittest.mock import patch
        parsed = {
            'region': '강원특별자치도', 'count': 3,
            'include_risk': True, 'include_history': False,
            'include_weather': True, 'include_detail': False,
            'start_date': None, 'end_date': None,
            'request_type': 'analysis', 'reasoning': '지역과 기상 요청을 확인함'
        }
        with patch('agent.nodes.llm.analyze_request', return_value=parsed):
            result = analyze_intent({'user_request': '강원도 위험 지역과 날씨 3곳', 'memory': [], 'session_id': 'llm-test'})
        self.assertEqual(result['intent']['region'], '강원특별자치도')
        self.assertEqual(result['intent']['count'], 3)
        self.assertTrue(result['intent']['include_weather'])
        self.assertTrue(result['llm_status']['used'])

    def test_missing_llm_key_falls_back_to_rules(self):
        with patch('agent.nodes.llm.analyze_request', side_effect=RuntimeError('OPENAI_API_KEY_NOT_CONFIGURED')):
            result = analyze_intent({'user_request': '강원도 산불 위험 지역 2곳', 'memory': [], 'session_id': 'fallback-test'})
        self.assertEqual(result['intent']['region'], '강원도')
        self.assertEqual(result['intent']['count'], 2)
        self.assertFalse(result['llm_status']['used'])
        self.assertEqual(result['llm_status']['source'], 'rules_fallback')

    def test_chat_does_not_call_tools(self):
        result=run_agent('안녕하세요',session_id='test-chat')
        self.assertEqual(result['selected_tools'],[])
        self.assertIn('안녕하세요',result['final_answer'])

    def test_tool_execution_and_answer(self):
        fake={'ok':True,'data':{'count':1,'items':[{'doname':'강원특별자치도','sigun':'춘천시','maxi':'80','meanavg':'60','sigucode':'51110'}]}}
        with patch.object(TOOLS['search_fire_risk'],'func',return_value=fake):
            s={'user_request':'강원도 산불 위험 지역 1곳','session_id':'test-run','memory':[]}
            s.update(analyze_intent(s)); s.update(create_plan(s)); s.update(execute_tools(s))
            a=assess_constraints(s)
            self.assertEqual(len(a['candidates']),1)
            self.assertIn('춘천시',generate_answer(s,a))

    def test_plan_crud_and_overlap(self):
        first=storage.create_plan({'title':'테스트 계획 A','region':'강원도','plan_date':'2099-01-01','start_time':'10:00','end_time':'11:00','details':{}})
        second=storage.create_plan({'title':'테스트 계획 B','region':'강원도','plan_date':'2099-01-01','start_time':'10:30','end_time':'11:30','details':{}})
        self.assertTrue(second['overlap'])
        self.assertTrue(storage.get_plan(first['id']))
        updated=storage.update_plan(first['id'],{'title':'수정 계획','region':'강원도','plan_date':'2099-01-01','start_time':'12:00','end_time':'13:00','details':{}})
        self.assertEqual(updated['title'],'수정 계획')
        self.assertTrue(storage.delete_plan(first['id'])); self.assertTrue(storage.delete_plan(second['id']))

if __name__=='__main__': unittest.main(verbosity=2)
