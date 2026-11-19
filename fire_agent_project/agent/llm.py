"""OpenAI LLM 어댑터. 키가 없거나 호출에 실패하면 호출부에서 규칙 기반으로 대체한다."""
import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class IntentSchema(BaseModel):
    region: str = Field(description="요청에서 확인된 지역명. 모호하거나 없으면 전국")
    count: int = Field(description="요청한 결과 개수. 없으면 5")
    include_risk: bool = Field(description="산불위험예보 조회 필요 여부")
    include_history: bool = Field(description="과거 산불 발생 기록 조회 필요 여부")
    include_weather: bool = Field(description="기상 관측자료 조회 필요 여부")
    include_detail: bool = Field(description="시군구 상세 조회 필요 여부")
    start_date: Optional[str] = Field(default=None, description="조회 시작일 YYYYMMDD. 요청에 날짜가 없으면 null")
    end_date: Optional[str] = Field(default=None, description="조회 종료일 YYYYMMDD. 요청에 날짜가 없으면 null")
    request_type: str = Field(description="일반 인사/사용법은 chat, 그 외는 analysis")
    reasoning: str = Field(description="요청에서 위 조건을 추출한 간단한 이유")


def is_configured() -> bool:
    return bool(os.getenv("OPENAI_API_KEY", "").strip())


def configured_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"


def configuration_status() -> dict:
    return {"enabled": is_configured(), "model": configured_model()}


@lru_cache(maxsize=4)
def _structured_model(model_name: str):
    # import를 지연해 LLM 패키지/키가 없어도 규칙 기반 서비스가 동작하게 한다.
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=model_name,
        temperature=0,
        api_key=os.environ["OPENAI_API_KEY"],
        timeout=20,
        max_retries=1,
    ).with_structured_output(IntentSchema)


def analyze_request(user_request: str, context: str = "") -> IntentSchema:
    if not is_configured():
        raise RuntimeError("OPENAI_API_KEY_NOT_CONFIGURED")
    prompt = (
        "사용자 요청에서 산불 정보 조회 의도를 구조화하세요. "
        "요청에 없는 지역·날짜·개수를 임의로 만들지 마세요. "
        "지역이 없으면 전국, 개수가 없으면 5로 두세요. "
        "산불위험예보, 과거 발생 기록, 기상 관측은 서로 다른 조회 의도입니다. "
        "단순 인사나 사용법 질문은 request_type=chat이며 모든 조회 플래그를 false로 둡니다. "
        "날짜가 명시된 경우에만 YYYYMMDD로 반환하고, 기간이 하나만 있으면 가능한 범위만 반환하세요.\n\n"
        f"이전 대화 문맥:\n{context or '(없음)'}\n\n"
        f"현재 사용자 요청:\n{user_request}"
    )
    return _structured_model(configured_model()).invoke(prompt)
