
from tools import TOOLS
import pprint


def find_items(data):
    """API 응답 내부에서 items 목록을 찾는다."""

    if isinstance(data, dict):
        if "items" in data:
            items = data["items"]

            if isinstance(items, list):
                return items

            if isinstance(items, dict):
                item = items.get("item", [])
                return item if isinstance(item, list) else [item]

        for value in data.values():
            result = find_items(value)

            if result is not None:
                return result

    return None


def test_region_code(code):

    print("\n" + "=" * 50)
    print(f"강원도 지역 코드 테스트: {code}")
    print("=" * 50)

    result = TOOLS["search_fire_risk"].run(
        sido_code=code
    )

    items = find_items(result)

    if items:
        print(f"조회 건수: {len(items)}")
        print("\n조회된 지역 샘플:")

        for item in items[:5]:
            print({
                "지역명": item.get("doname"),
                "시군구": item.get("sigun"),
                "지역코드": item.get("regioncode"),
                "시군구코드": item.get("sigucode"),
            })

    else:
        print("조회된 items가 없습니다.")
        pprint.pprint(result, depth=3)


if __name__ == "__main__":

    test_region_code("42")
    test_region_code("51")
