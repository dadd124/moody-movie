def chatbot():
    responses = {
        "날씨": "오늘 날씨는 맑아요 ☀️",
        "시간": "현재 시간은 오후 3시입니다 🕒",
        "이름": "저는 챗봇이에요 🤖",
    }

    while True:
        user_input = input("사용자: ")

        if user_input in ["종료", "끝", "exit"]:
            print("챗봇: 대화 종료할게요 👋")
            break

        found = False
        for keyword, answer in responses.items():
            if keyword in user_input:
                print("챗봇:", answer)
                found = True
                break

        if not found:
            print("챗봇: 잘 모르겠어요 😅 다시 말씀해 주실래요?")