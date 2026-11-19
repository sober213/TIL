from fastapi import APIRouter, HTTPException
import storage
router=APIRouter(prefix='/api/logs',tags=['execution-logs'])

@router.get('')
def list_all(limit:int=100): return {'ok':True,'data':storage.list_logs(max(1,min(limit,500)))}

@router.get('/{session_id}')
def detail(session_id:str):
    events=storage.get_logs(session_id)
    if not events: raise HTTPException(404,'실행 로그를 찾을 수 없습니다.')
    return {'ok':True,'data':events}

@router.delete('/{session_id}')
def delete(session_id:str):
    count=storage.delete_logs(session_id)
    if not count: raise HTTPException(404,'삭제할 실행 로그가 없습니다.')
    return {'ok':True,'data':{'deleted_count':count}}
