# Tool 정의서

모든 Tool은 성공 시 `{"ok": true, "data": ...}`, 실패 시 `{"ok": false, "error": {"code": "...", "message": "..."}}`를 반환한다.

| Tool | 입력 | 용도 | 출처 |
|---|---|---|---|
| `search_fire_risk` | 선택: `sido_code`, `sigungu_code` | 지역별 산불위험예보 후보 조회 | 공공데이터포털 산림청 산불위험예보정보 API, `forestPointListSigunguSearchV2` |
| `search_fire_risk_detail` | 필수: `sigungu_code` | 특정 시군구의 산불위험예보 속성 상세 조회 | 위와 동일한 산림청 API의 시군구 필터 조회 |
| `search_fire_history` | `start_date`, `end_date` (YYYYMMDD) | 기간별 산불 발생 이력 | 공공데이터포털 산림청 산불 발생 통계 API |
| `search_weather` | `start_date`, `end_date`, 선택: `station` 또는 `stations` | ASOS 평균기온·습도·강수량·풍속 관측자료 | 기상청 ASOS 일자료 조회 API |

## 주요 실패 코드

- `BAD_ARGUMENT`: 필수값/형식 오류
- `INVALID_KEY`: 인증키 환경변수 누락
- `NO_DATA`: 조회 결과 없음
- `NO_REGION_DATA`: 전국/지역 조회 결과에서 요청 지역을 확인하지 못함
- `UPSTREAM_ERROR`: 외부 API 통신/응답 오류
- `UNKNOWN_TOOL`: 등록되지 않은 Tool

환경변수 이름은 `FIRE_RISK_API_KEY`, `FIRE_HISTORY_API_KEY`, `ASOS_API_KEY`이다. 실제 호출 한도와 이용 조건은 각 API의 공공데이터포털 상세 페이지 및 이용 신청 조건을 프로젝트 제출 전에 확인한다.
