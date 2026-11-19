# API 명세

기본 주소: `http://127.0.0.1:8000`

## 대화

`POST /api/chat`

요청: `{"message":"강원도 산불 위험 지역 5곳","session_id":null}`
응답: `ok`, `session_id`, `answer`, `intent`, `plan`, `selected_tools`, `tool_results`, `assessment`, `execution_logs`, `execution_events`, `retry_count`.

## 계획

- `GET /api/plans`: 목록
- `POST /api/plans`: 저장. 필드 `title`, `region`, `plan_date`(YYYY-MM-DD), `start_time`, `end_time`, `details`
- `GET /api/plans/{id}`: 상세
- `PUT /api/plans/{id}`: 핵심 값 수정
- `DELETE /api/plans/{id}`: 삭제

같은 날짜/시간이 겹쳐도 저장하며 응답의 `overlap`, `overlapping_plan_ids`로 알린다.

## 실행 로그

- `GET /api/logs?limit=100`: 세션별 목록
- `GET /api/logs/{session_id}`: 해당 세션 이벤트 상세(발생 순)
- `DELETE /api/logs/{session_id}`: 해당 세션 로그 삭제

로그 수정 API는 제공하지 않는다.

## 기타

- `GET /api/tools`: Tool 명세 목록
- `GET /api/health`: 서버 상태
- `/docs`: FastAPI OpenAPI 문서
