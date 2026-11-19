from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import storage

router=APIRouter(prefix='/api/plans',tags=['plans'])

class PlanInput(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    region: Optional[str] = None
    plan_date: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    details: dict = Field(default_factory=dict)

@router.post('')
def create(data:PlanInput):
    return {'ok':True,'data':storage.create_plan(data.model_dump())}

@router.get('')
def list_all(): return {'ok':True,'data':storage.list_plans()}

@router.get('/{plan_id}')
def detail(plan_id:int):
    item=storage.get_plan(plan_id)
    if not item: raise HTTPException(404,'계획을 찾을 수 없습니다.')
    return {'ok':True,'data':item}

@router.put('/{plan_id}')
def update(plan_id:int,data:PlanInput):
    item=storage.update_plan(plan_id,data.model_dump())
    if not item: raise HTTPException(404,'계획을 찾을 수 없습니다.')
    return {'ok':True,'data':item}

@router.delete('/{plan_id}')
def delete(plan_id:int):
    if not storage.delete_plan(plan_id): raise HTTPException(404,'계획을 찾을 수 없습니다.')
    return {'ok':True,'data':{'deleted':True,'id':plan_id}}
