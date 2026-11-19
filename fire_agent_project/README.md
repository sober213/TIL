# ForestGuard AI — 산불 고위험 지역 예측 Agent

산불위험예보, 과거 산불 발생 기록, 기상청 ASOS 관측자료를 Tool로 조회하고, 결과와 실행 과정을 함께 제공하는 FastAPI 기반 프로젝트입니다.

> 중요: 이 서비스는 공식 산불위험예보와 관측자료를 조회·정리합니다. API가 제공하지 않는 산불 발생 확률을 임의 계산하지 않으며, 산불 대응·대피 판단은 산림청 및 관계기관의 최신 안내를 우선해야 합니다.

## 1. 구성

```text
fire_agent_project/
├─ agent/
│  ├─ graph.py          # LangGraph 실행 그래프 및 fallback
│  ├─ nodes.py          # 의도 분석, 계획, Tool 실행, 제약 판단, 응답
│  ├─ state.py          # Agent 상태
│  └─ events.py         # 실행 이벤트 발행/구독
├─ api/
│  ├─ plans.py          # 계획 CRUD API
│  └─ logs.py           # 실행 로그 조회/삭제 API
├─ web/                 # HTML/CSS/JS 프론트엔드
├─ data/                # SQLite DB 자동 생성
├─ tools.py             # 외부 API Tool 정의와 등록
├─ storage.py           # SQLite 저장소
├─ main.py              # FastAPI 진입점
├─ .env.example         # 환경변수 예시
└─ requirements.txt
```

## 2. 설치 및 실행

Python 3.10 이상 권장. 프로젝트 폴더에서 아래 명령을 실행합니다.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows CMD라면: .venv\Scripts\activate.bat
pip install -r requirements.txt
```

`.env.example`을 복사해 `.env`로 이름을 바꾸고 공공데이터포털에서 발급한 서비스키를 입력합니다. OpenAI 요청 분석을 사용하려면 아래 선택 항목도 설정합니다.

```env
FIRE_HISTORY_API_KEY=발급키
FIRE_RISK_API_KEY=발급키
ASOS_API_KEY=발급키

# 선택: LLM 기반 사용자 요청 분석
OPENAI_API_KEY=발급받은_OpenAI_API_키
OPENAI_MODEL=gpt-4o-mini
```

OpenAI 키가 설정되면 LLM이 지역·조회 종류·개수·기간을 구조화합니다. 키가 없거나 호출에 실패하면 기존 규칙 기반 분석으로 자동 대체되며, 서버와 화면은 계속 실행됩니다. 공공데이터 API 키가 없으면 해당 외부 조회는 `INVALID_KEY`로 실패하고 화면에는 키 자체가 노출되지 않습니다.

```bash
uvicorn main:app --reload
```

- 화면: http://127.0.0.1:8000
- API 문서: http://127.0.0.1:8000/docs
- 상태 확인: http://127.0.0.1:8000/api/health

## 3. API 목록

| Method | Path | 설명 |
|---|---|---|
| POST | `/api/chat` | Agent 대화/분석 실행 |
| GET | `/api/tools` | 등록 Tool 명세 |
| GET/POST | `/api/plans` | 계획 목록/저장 |
| GET/PUT/DELETE | `/api/plans/{id}` | 계획 상세/수정/삭제 |
| GET | `/api/logs` | 세션별 로그 목록 |
| GET/DELETE | `/api/logs/{session_id}` | 세션 로그 상세/삭제 |
| GET | `/api/health` | 서버 상태 |

대화 요청 예시:

```json
{
  "message": "강원도 산불 위험이 높은 지역 5곳과 기상 자료를 확인해줘",
  "session_id": null
}
```

응답에는 `answer`, `intent`, `plan`, `selected_tools`, `tool_results`, `assessment`, `execution_logs`, `retry_count`, `llm_status`가 포함됩니다. `/api/health`에서도 LLM 설정 여부와 모델명을 확인할 수 있습니다.

## 4. 등록 Tool

- `search_fire_risk`: 시도/시군구 산불위험예보 후보 조회
- `search_fire_risk_detail`: 특정 시군구의 산불위험예보 상세 조회용 Tool
- `search_fire_history`: 기간별 산불 발생 기록 조회
- `search_weather`: ASOS 일자료 조회. 단일 관측소 또는 복수 관측소 지원

모든 Tool은 `{"ok": true, "data": ...}` 또는 `{"ok": false, "error": {"code": ..., "message": ...}}` 형식으로 반환합니다.

## 5. 지역 코드 및 기상 관측소

현재 확인한 API 응답을 기준으로 강원특별자치도 코드는 `51`이며, 강원권 기상 관측소는 속초(90), 춘천(101), 강릉(105), 동해(106), 원주(114), 영월(121), 인제(211), 태백(216)을 사용합니다. 다른 시도 코드는 API 데이터 제공 범위와 실제 응답을 추가 확인해야 합니다. 지역 코드가 조회되지 않으면 전국 후보 조회로 한 번 보완하며, 지역명이 결과에 확인되지 않으면 해당 지역 후보로 단정하지 않습니다.

## 6. 저장 및 실행 로그

SQLite DB는 첫 실행 시 `data/fire_agent.db`로 자동 생성됩니다. 계획은 날짜/시간 중복이 있어도 저장하며 중복 계획 ID를 응답에 알립니다. 실행 이벤트는 세션별로 저장하며, 원본 이벤트는 LLM으로 요약·수정하지 않습니다. 실행 로그는 목록/상세/삭제만 제공하고 수정 API는 제공하지 않습니다.

## 7. 확인 및 한계

- Python 문법 컴파일 및 모듈 import 확인을 수행했습니다.
- 외부 API는 실제 키와 네트워크가 있어야 통합 호출 검증이 가능합니다.
- 위험 지수의 세부 필드 의미와 공식 등급 구간은 API 제공기관 정의를 확인하기 전까지 임의 해석하지 않습니다.
- 현재 재계획은 지역별 위험예보 조회가 비었을 때 전국 조회로 한 번 보완하는 규칙 기반 경로입니다. 일반적인 후보 최적화 반복 탐색은 구현 범위에 포함하지 않았습니다.
- 대화 맥락은 세션의 최근 메시지를 제한적으로 보존합니다. 후속 요청에서 “같은 조건”, “그 지역” 등 문맥 표현이 있을 때 직전 사용자 요청을 조건 추출에 활용합니다.
- F3020~F3023은 심화 기능이며 필수 기능 F3001~F3019 완료 이후 별도 구현 대상입니다. 본 프로젝트는 필수 기능에 집중합니다.

## 8. 보안

`.env`, `data/`, `.venv/`, `__pycache__/`는 Git에 올리지 않습니다. API 키는 코드에 입력하지 마세요.
