
import os
import requests
import xml.etree.ElementTree as ET

from dotenv import load_dotenv

# 1. .env 파일 불러오기
load_dotenv()

# 2. API 기본 정보
API_URL = (
    "https://apis.data.go.kr/"
    "1400000/forestStusService/getfirestatsservice"
)

API_KEY = os.getenv("FIRE_HISTORY_API_KEY")


# 3. API 호출 함수
def search_fire_history(start_date, end_date):

    # 인증키 확인
    if not API_KEY:
        return {
            "ok": False,
            "error": {
                "code": "INVALID_KEY",
                "message": "API 인증키가 없습니다."
            }
        }

    # 입력값 확인
    if not start_date or not end_date:
        return {
            "ok": False,
            "error": {
                "code": "BAD_ARGUMENT",
                "message": "조회 기간을 입력해야 합니다."
            }
        }

    # API 요청에 필요한 파라미터
    params = {
        "serviceKey": API_KEY,
        "numOfRows": 10,
        "pageNo": 1,
        "searchStDt": start_date,
        "searchEdDt": end_date
    }

    try:
        # 4. API 호출
        response = requests.get(
            API_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        # 5. XML 응답 파싱
        root = ET.fromstring(response.content)

        # API 오류 확인
        result_code = root.findtext(".//resultCode")

        if result_code and result_code != "00":
            return {
                "ok": False,
                "error": {
                    "code": "UPSTREAM_ERROR",
                    "message": root.findtext(".//resultMsg")
                }
            }

        # 6. 산불 발생 기록 추출
        items = root.findall(".//item")

        if not items:
            return {
                "ok": False,
                "error": {
                    "code": "NO_DATA",
                    "message": "조회된 산불 기록이 없습니다."
                }
            }

        # 7. 필요한 정보만 추출
        fire_records = []

        for item in items:
            fire_records.append({
                "year": item.findtext("startyear"),
                "month": item.findtext("startmonth"),
                "day": item.findtext("startday"),
                "time": item.findtext("starttime"),
                "sido": item.findtext("locsi"),
                "sigungu": item.findtext("locgungu"),
                "cause": item.findtext("firecause"),
                "damage_area": item.findtext("damagearea")
            })

        return {
            "ok": True,
            "data": {
                "start_date": start_date,
                "end_date": end_date,
                "count": len(fire_records),
                "items": fire_records
            }
        }

    except requests.RequestException:
        return {
            "ok": False,
            "error": {
                "code": "UPSTREAM_ERROR",
                "message": "외부 API 호출에 실패했습니다."
            }
        }

    except ET.ParseError:
        return {
            "ok": False,
            "error": {
                "code": "PARSE_ERROR",
                "message": "API 응답 XML을 해석하지 못했습니다."
            }
        }


# 8. 직접 실행했을 때 테스트
if __name__ == "__main__":

    result = search_fire_history(
        start_date="20250101",
        end_date="20251231"
    )

    print(result)
