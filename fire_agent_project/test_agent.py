
from agent.nodes import (
    analyze_intent,
    create_plan,
    execute_tools,
)


def main():

    # =====================================
    # 1. Agent 초기 상태 생성
    # =====================================

    state = {
        "user_request": (
            "강원도에서 산불 위험이 높은 지역 5곳을 찾고 "
            "과거 산불 발생 이력과 기상 상황도 분석해 줘."
        ),

        "intent": {},
        "plan": [],
        "selected_tools": [],
        "tool_results": {},

        "constraints_satisfied": False,
        "retry_count": 0,
        "max_retries": 3,

        "final_answer": "",
        "execution_logs": [],
    }

    print("=" * 50)
    print("ForestGuard AI - Agent 테스트")
    print("=" * 50)


    # =====================================
    # 2. 사용자 요청 분석
    # =====================================

    print("\n[1단계] 사용자 요청 분석")

    result = analyze_intent(state)
    state.update(result)

    print("분석된 의도:")
    print(state["intent"])


    # =====================================
    # 3. 실행 계획 생성
    # =====================================

    print("\n[2단계] 실행 계획 생성")

    result = create_plan(state)
    state.update(result)

    print("\n선택된 Tool:")
    print(state["selected_tools"])

    print("\n실행 계획:")

    for step in state["plan"]:
        print(f"\nTool: {step['tool']}")
        print(f"목적: {step['purpose']}")
        print(f"필요 조건: {step.get('needs', [])}")
        print(f"인자: {step.get('arguments', {})}")


    # =====================================
    # 4. Tool 실행
    # =====================================

    print("\n[3단계] Tool 실행")

    result = execute_tools(state)
    state.update(result)

    print("\nTool 실행 결과:")

    for tool_name, tool_result in state["tool_results"].items():
        print(f"\nTool: {tool_name}")
        print(tool_result)


    # =====================================
    # 5. 실행 로그 출력
    # =====================================

    print("\n[4단계] 실행 로그")

    for log in state["execution_logs"]:
        print(log)

    

    # =====================================
    # 6. 최종 상태 확인
    # =====================================

    print("\n[5단계] 최종 Agent 상태")

    print("선택된 Tool:", state["selected_tools"])
    print("실행된 결과 수:", len(state["tool_results"]))
    print("재시도 횟수:", state["retry_count"])

    print("\n테스트 종료")




if __name__ == "__main__":
    main()

    