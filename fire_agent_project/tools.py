
"""
국내 산불 발생 기록 조회 Tool

실행:
    python tools.py
"""

import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Callable

import requests
from dotenv import load_dotenv

load_dotenv()

# ── ① 약속: 성공도 실패도 같은 모양 ──────────────────────────

def ok(data):
    return {"ok": True, "data": data}


def fail(code, message):
    return {"ok": False, "error": {"code": code, "message": message}}


# ── ② Tool 명함 ─────────────────────────────────────────────

@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    func: Callable

    def run(self, **kwargs):
        try:
            return self.func(**kwargs)
        except TypeError:
            return fail("BAD_ARGUMENT", "입력값이 규약과 다릅니다.")
        except Exception:
            return fail("UPSTREAM_ERROR", "Tool 실행 중 오류입니다.")


# ── ③ 산불 발생 기록 조회 API ───────────────────────────────

API_URL = (
    "https://apis.data.go.kr/1400000/"
    "forestStusService/getfirestatsservice"
)

KEY_NAME = "FIRE_HISTORY_API_KEY"


def search_fire_history(start_date: str, end_date: str):
    """
    입력한 기간의 국내 산불 발생 기록을 조회한다.

    start_date: 조회 시작일 (YYYYMMDD)
    end_date: 조회 종료일 (YYYYMMDD)
    """

    # 필수 입력값 확인
    if not start_date or not end_date:
        return fail("BAD_ARGUMENT", "조회 시작일과 종료일은 필수입니다.")

    # 날짜 형식 확인
    if (
        len(start_date) != 8
        or len(end_date) != 8
        or not start_date.isdigit()
        or not end_date.isdigit()
        or start_date > end_date
    ):
        return fail("BAD_ARGUMENT", "날짜는 YYYYMMDD 형식이어야 합니다.")

    # 인증키 확인
    key = os.getenv(KEY_NAME)

    if not key:
        return fail("INVALID_KEY", f"{KEY_NAME}가 없습니다.")

    # API 요청
    params = {
        "serviceKey": key,
        "numOfRows": 100,
        "pageNo": 1,
        "searchStDt": start_date,
        "searchEdDt": end_date,
    }

    try:
        res = requests.get(
            API_URL,
            params=params,
            timeout=15
        )

        res.raise_for_status()

        root = ET.fromstring(res.content)

    except requests.RequestException:
        return fail("UPSTREAM_ERROR", "산불 발생 기록 API 호출에 실패했습니다.")

    except ET.ParseError:
        return fail("UPSTREAM_ERROR", "API 응답 XML을 해석하지 못했습니다.")

    # API 응답 상태 확인
    result_code = root.findtext(".//resultCode")

    if result_code and result_code != "00":
        return fail(
            "UPSTREAM_ERROR",
            root.findtext(".//resultMsg") or "API에서 오류를 반환했습니다."
        )

    # 산불 발생 기록 추출
    items = root.findall(".//item")

    if not items:
        return fail("NO_DATA", "해당 기간의 산불 발생 기록이 없습니다.")

    fire_records = []

    for item in items:
        fire_records.append({
            "year": item.findtext("startyear"),
            "month": item.findtext("startmonth"),
            "day": item.findtext("startday"),
            "time": item.findtext("starttime"),
            "sido": item.findtext("locsi"),
            "sigungu": item.findtext("locgungu"),
            "dong": item.findtext("locdong"),
            "cause": item.findtext("firecause"),
            "damage_area": item.findtext("damagearea"),
        })

    return ok({
        "start_date": start_date,
        "end_date": end_date,
        "count": len(fire_records),
        "items": fire_records,
    })


# ── 산불위험예보정보 API ─────────────────────────────────────

FIRE_RISK_API_URL = (
    "https://apis.data.go.kr/1400377/"
    "forestPointV2/forestPointListSigunguSearchV2"
)

FIRE_RISK_KEY_NAME = "FIRE_RISK_API_KEY"


def search_fire_risk(
    sigungu_code: str = None,
    sido_code: str = None
):
    """
    시군구별 산불위험예보정보 조회

    sigungu_code: 시군구 코드 5자리 (선택)
    sido_code: 시도 코드 2자리 (선택)
    """

    # 입력값 검증
    if sigungu_code and (
        len(sigungu_code) != 5 or not sigungu_code.isdigit()
    ):
        return fail("BAD_ARGUMENT", "시군구 코드는 숫자 5자리여야 합니다.")

    if sido_code and (
        len(sido_code) != 2 or not sido_code.isdigit()
    ):
        return fail("BAD_ARGUMENT", "시도 코드는 숫자 2자리여야 합니다.")

    key = os.getenv(FIRE_RISK_KEY_NAME)

    if not key:
        return fail("INVALID_KEY", "산불위험예보 API 인증키가 없습니다.")

    params = {
        "serviceKey": key,
        "pageNo": 1,
        "numOfRows": 100,
        "_type": "json",
        "excludeForecast": "0",
    }

    if sigungu_code:
        params["localAreas"] = sigungu_code

    if sido_code:
        params["upplocalcd"] = sido_code

    try:
        res = requests.get(
            FIRE_RISK_API_URL,
            params=params,
            timeout=15
        )

        res.raise_for_status()
        body = res.json()

    except requests.RequestException:
        return fail("UPSTREAM_ERROR", "산불위험예보 API 호출에 실패했습니다.")

    except ValueError:
        return fail("UPSTREAM_ERROR", "API JSON 응답을 해석하지 못했습니다.")

    # 응답 구조 확인
    response = body.get("response", body)
    header = response.get("header", {})

    result_code = str(header.get("resultCode", ""))

    if result_code and result_code != "00":
        return fail(
            "UPSTREAM_ERROR",
            header.get("resultMsg", "산불위험예보 API 오류")
        )

    response_body = response.get("body", response)
    items_data = response_body.get("items", [])

    if isinstance(items_data, dict):
        items = items_data.get("item", [])
    else:
        items = items_data

    if isinstance(items, dict):
        items = [items]

    if not items:
        return fail("NO_DATA", "조회된 산불위험예보정보가 없습니다.")

    # 분석에 필요한 값만 추출
    risk_records = []

    fields = [
        "analdate",
        "doname",
        "sigun",
        "regioncode",
        "sigucode",
        "maxi",
        "meanavg",
        "mini",
        "std",
        "d1",
        "d2",
        "d3",
        "d4",
    ]

    for item in items:
        record = {}

        for field in fields:
            value = item.get(field)

            if value is not None and value != "":
                record[field] = value

        risk_records.append(record)

    return ok({
        "count": len(risk_records),
        "items": risk_records,
    })


def search_fire_risk_detail(sigungu_code: str):
    """특정 시군구의 산불위험예보 속성을 상세 조회한다."""
    if not sigungu_code:
        return fail("BAD_ARGUMENT", "시군구 코드가 필요합니다.")
    return search_fire_risk(sigungu_code=sigungu_code)


# ── 기상청 ASOS 일자료 조회 API ──────────────────────────────

WEATHER_API_URL = (
    "https://apis.data.go.kr/1360000/"
    "AsosDalyInfoService/getWthrDataList"
)

WEATHER_KEY_NAME = "ASOS_API_KEY"



def search_weather(
    start_date: str,
    end_date: str,
    station: str = "108",
    stations: list = None
):
    """
    기상청 ASOS 일자료 조회

    station: 단일 관측소 번호
    stations: 여러 관측소 번호 목록
    """

    # 입력값 검증
    if not start_date or not end_date:
        return fail("BAD_ARGUMENT", "조회 시작일과 종료일은 필수입니다.")

    if (
        len(start_date) != 8
        or len(end_date) != 8
        or not start_date.isdigit()
        or not end_date.isdigit()
        or start_date > end_date
    ):
        return fail("BAD_ARGUMENT", "날짜는 YYYYMMDD 형식이어야 합니다.")

    # 여러 관측소 조회
    if stations is not None:

        if not isinstance(stations, list) or not stations:
            return fail("BAD_ARGUMENT", "관측소 목록이 올바르지 않습니다.")

        stations = list(dict.fromkeys(str(s) for s in stations))

        if any(not s.isdigit() for s in stations):
            return fail("BAD_ARGUMENT", "관측소 번호를 확인해 주세요.")

        station_names = {
            "90": "속초",
            "101": "춘천",
            "105": "강릉",
            "106": "동해",
            "114": "원주",
            "121": "영월",
            "211": "인제",
            "216": "태백",
        }

        all_records = []
        success_stations = []
        failed_stations = []

        for station_code in stations:

            result = search_weather(
                start_date=start_date,
                end_date=end_date,
                station=station_code,
            )

            if result.get("ok") is True:

                records = result["data"]["items"]

                for record in records:
                    record["station_name"] = station_names.get(
                        station_code,
                        "알 수 없는 관측소"
                    )

                all_records.extend(records)
                success_stations.append(station_code)

            else:
                failed_stations.append({
                    "station": station_code,
                    "reason": result.get("error", {})
                })

        if not all_records:
            return fail(
                "NO_DATA",
                "모든 관측소에서 기상자료를 조회하지 못했습니다."
            )

        return ok({
            "start_date": start_date,
            "end_date": end_date,
            "stations": stations,
            "success_stations": success_stations,
            "failed_stations": failed_stations,
            "station_count": len(success_stations),
            "count": len(all_records),
            "items": all_records,
        })

    # 단일 관측소 조회
    if not station or not station.isdigit():
        return fail("BAD_ARGUMENT", "관측소 번호를 확인해 주세요.")

    key = os.getenv(WEATHER_KEY_NAME)

    if not key:
        return fail("INVALID_KEY", "ASOS API 인증키가 없습니다.")

    params = {
        "serviceKey": key,
        "pageNo": 1,
        "numOfRows": 100,
        "dataType": "JSON",
        "dataCd": "ASOS",
        "dateCd": "DAY",
        "startDt": start_date,
        "endDt": end_date,
        "stnIds": station,
    }

    try:
        res = requests.get(
            WEATHER_API_URL,
            params=params,
            timeout=15
        )

        res.raise_for_status()
        body = res.json()

    except requests.RequestException:
        return fail("UPSTREAM_ERROR", "기상청 API 호출에 실패했습니다.")

    except ValueError:
        return fail("UPSTREAM_ERROR", "기상청 JSON 응답을 해석하지 못했습니다.")

    response = body.get("response", {})
    header = response.get("header", {})

    result_code = str(header.get("resultCode", ""))

    if result_code and result_code != "00":
        return fail(
            "UPSTREAM_ERROR",
            header.get("resultMsg", "기상청 API 오류")
        )

    data_body = response.get("body", {})
    items_data = data_body.get("items", {})
    items = items_data.get("item", []) if isinstance(items_data, dict) else []

    if isinstance(items, dict):
        items = [items]

    if not items:
        return fail("NO_DATA", "조회된 기상자료가 없습니다.")

    weather_records = []

    for item in items:
        record = {
            "date": item.get("tm"),
            "station": item.get("stnId"),
        }

        fields = {
            "avg_temperature": "avgTa",
            "avg_humidity": "avgRhm",
            "daily_rainfall": "sumRn",
            "avg_wind_speed": "avgWs",
        }

        for output_name, api_name in fields.items():
            value = item.get(api_name)

            if value is not None and value != "":
                record[output_name] = value

        weather_records.append(record)

    return ok({
        "start_date": start_date,
        "end_date": end_date,
        "station": station,
        "count": len(weather_records),
        "items": weather_records,
    })





# ── ④ Tool 등록 ─────────────────────────────────────────────

TOOLS = {
    tool.name: tool
    for tool in [
        Tool(
            name="search_fire_history",

            description=(
                "특정 기간의 국내 산불 발생 기록을 조회할 때 사용한다. "
                "산불 발생 지역, 발생 일자, 발생 원인, 피해 면적을 확인한다."
            ),

            parameters={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "조회 시작일 YYYYMMDD"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "조회 종료일 YYYYMMDD"
                    },
                },
                "required": ["start_date", "end_date"],
            },

            func=search_fire_history,
        ), 

        Tool(
            name="search_fire_risk",

            description=(
                "전국 또는 특정 시도·시군구의 산불위험예보를 조회할 때 사용한다. "
                "지역별 산불위험지수와 예보 정보를 확인한다."
            ),

            parameters={
                "type": "object",
                "properties": {
                    "sigungu_code": {
                        "type": "string",
                        "description": "시군구 코드 5자리"
                    },
                    "sido_code": {
                        "type": "string",
                        "description": "시도 코드 2자리"
                    }
                },
                "required": []
            },

            func=search_fire_risk,
        ),

        Tool(
            name="search_fire_risk_detail",
            description=(
                "산불위험예보 후보 목록에서 선택한 특정 시군구의 위험예보 속성을 확인할 때 사용한다."
            ),
            parameters={
                "type": "object",
                "properties": {"sigungu_code": {"type": "string", "description": "시군구 코드 5자리"}},
                "required": ["sigungu_code"],
            },
            func=search_fire_risk_detail,
        ),

        Tool(
            name="search_weather",

            description=(
                "특정 기간과 관측소의 기상 관측자료를 조회할 때 사용한다. "
                "평균 기온, 평균 상대습도, 일강수량, 평균 풍속을 확인한다."
            ),

            parameters={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "조회 시작일 YYYYMMDD"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "조회 종료일 YYYYMMDD"
                    },
                    "station": {
                        "type": "string",
                        "description": "기상 관측소 번호. 기본값은 서울 108"
                    },
                    "stations": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "여러 관측소 번호 목록. 지정하면 station 대신 사용"
                    }
                },
                "required": ["start_date", "end_date"]
            },

            func=search_weather,
        ),

    ]
}


def catalog():
    """Agent에게 전달할 Tool 목록"""

    return [
        {
            "name": t.name,
            "description": t.description,
            "parameters": t.parameters,
        }
        for t in TOOLS.values()
    ]


# ── 시험 호출 ────────────────────────────────────────────────


if __name__ == "__main__":

    # 등록된 Tool 목록 확인
    for c in catalog():
        print("[Tool]", c["name"], "—", c["description"])

    print("\n===== Tool 실행 테스트 =====")

    # 1. 산불 발생 이력
    history_result = TOOLS["search_fire_history"].run(
        start_date="20250101",
        end_date="20251231"
    )

    print("\n[산불 발생 이력]")
    print(history_result)

    # 2. 산불 위험 예보
    risk_result = TOOLS["search_fire_risk"].run()

    print("\n[산불 위험 예보]")
    print(risk_result)

    # 3. 기상 관측자료
    weather_result = TOOLS["search_weather"].run(
        start_date="20250101",
        end_date="20250107",
        station="108"
    )

    print("\n[기상 관측자료]")
    print(weather_result)

