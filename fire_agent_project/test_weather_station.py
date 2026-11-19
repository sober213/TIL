
from tools import search_weather
import pprint

result = search_weather(
    start_date="20261020",
    end_date="20261118",
    stations=[
        "90",
        "101",
        "105",
        "106",
        "114",
        "121",
        "211",
        "216",
    ],
)

print("=== 강원도 복수 관측소 조회 결과 ===")
pprint.pprint(result, depth=4)

if result.get("ok"):
    data = result["data"]

    print("\n=== 조회 요약 ===")
    print("성공 관측소:", data["success_stations"])
    print("실패 관측소:", data["failed_stations"])
    print("성공 관측소 수:", data["station_count"])
    print("전체 데이터 수:", data["count"])
