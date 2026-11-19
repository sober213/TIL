from uuid import uuid4
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Optional
import storage
from agent.graph import run_agent
from agent.llm import configuration_status
from agent.events import subscribe
from api.plans import router as plans_router
from api.logs import router as logs_router
import logging

app=FastAPI(title='산불 고위험 지역 예측 Agent',version='1.0.0',description='산불위험예보·과거 산불기록·기상 관측자료를 통합 조회하는 Agent 서비스')
app.include_router(plans_router); app.include_router(logs_router)
subscribe(storage.save_event)

class ChatRequest(BaseModel):
    message:str=Field(min_length=1,max_length=3000)
    session_id:Optional[str]=None

@app.get('/api/health')
def health(): return {'ok':True,'service':'fire-risk-agent','llm':configuration_status()}

@app.get('/api/tools')
def tools_catalog():
    from tools import catalog
    return {'ok':True,'data':catalog()}

@app.post('/api/chat')
def chat(req:ChatRequest):
    sid=req.session_id or str(uuid4())
    try:
        memory=storage.get_memory(sid)
        # 최근 대화의 조건을 후속 요청에 활용할 수 있도록 기록. 사용자 메시지는 원문 그대로 보존.
        result=run_agent(req.message,session_id=sid,memory=memory)
        memory=(memory+[{'role':'user','content':req.message},{'role':'assistant','content':result.get('final_answer','')}])[-12:]
        storage.save_memory(sid,memory)
        return {'ok':True,'session_id':sid,'answer':result.get('final_answer',''),
          'intent':result.get('intent',{}),'plan':result.get('plan',[]),'selected_tools':result.get('selected_tools',[]),
          'tool_results':result.get('tool_results',{}),'assessment':result.get('assessment',{}),
          'execution_logs':result.get('execution_logs',[]),'execution_events':storage.get_logs(sid),'retry_count':result.get('retry_count',0),'llm_status':result.get('llm_status',{'used':False,'source':'rules'})}
    except Exception:
        logging.exception("POST /api/chat 처리 실패")
        raise HTTPException(
            500,
            '요청 처리 중 오류가 발생했습니다. 서버 로그를 확인해 주세요.'
        )

WEB_DIR=Path(__file__).resolve().parent/'web'
if WEB_DIR.exists():
    app.mount('/static',StaticFiles(directory=WEB_DIR),name='static')
    @app.get('/')
    def index(): return FileResponse(WEB_DIR/'index.html')
