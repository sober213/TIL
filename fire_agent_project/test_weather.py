
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = (
    "https://apis.data.go.kr/1360000/"
    "AsosDalyInfoService/getWthrDataList"
)

KEY_NAME = "ASOS_API_KEY"


def search_weather(start_date, end_date, station="108"):

    key = os.getenv(KEY_NAME)

    if not key:
        return {
            "ok": False,
            "error": "인증키가 없습니다."
        }

    if (
        len(start_date) != 8
        or len(end_date) != 8
        or not start_date.isdigit()
        or not end_date.isdigit()
        or start_date > end_date
    ):
        return {
            "ok": False,
            "error": "날짜는 YYYYMMDD 형식이어야 합니다."
        }

    params = {
        "serviceKey": key,
        "pageNo": 1,
        "numOfRows": 10,
        "dataType": "JSON",
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "startDt": start_date,
        "endDt": end_date,
        "stnIds": station,
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()
        body = response.json()

    except requests.RequestException:
        return {
            "ok": False,
            "error": "기상청 API 호출에 실패했습니다."
        }

    except ValueError:
        return {
            "ok": False,
            "error": "JSON 응답을 해석하지 못했습니다."
        }

    # 응답 구조 확인
    response_body = body.get("response", {})
    header = response_body.get("header", {})

    if str(header.get("resultCode", "")) != "00":
        return {
            "ok": False,
            "error": header.get("resultMsg", "API 오류")
        }

    data_body = response_body.get("body", {})
    items = data_body.get("items", {}).get("item", [])

    if isinstance(items, dict):
        items = [items]

    if not items:
        return {
            "ok": False,
            "error": "조회된 기상자료가 없습니다."
        }

    weather_records = []

    for item in items:
        weather_records.append({
            "date": item.get("tm"),
            "station": item.get("stnId"),
            "avg_temperature": item.get("avgTa"),
            "avg_humidity": item.get("avgRhm"),
            "daily_rainfall": item.get("sumRn"),
            "avg_wind_speed": item.get("avgWs"),
        })

    return {
        "ok": True,
        "data": {
            "count": len(weather_records),
            "items": weather_records
        }
    }


if __name__ == "__main__":

    result = search_weather(
        start_date="20250101",
        end_date="20250107",
        station="108"
    )

    print(result)
