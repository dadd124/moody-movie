
def main_menu():
    while True:
        print("\n지금 테스트 중이야.")

        user_input = input("뭐든 말 좀 해봐: ")
        if user_input == "0":
            first()
        elif user_input == "1":
            second()
        else:
            print("인정할게. 너의 참신함에 졌어. 할 말이 없네.")
            break

def first():
    while True:
        user_input = input("이 길도 길이지. ")

        if user_input == "0":
            print("뚜렷한 감정이 없는 날도 있지. 그럼 이건 어때?")
        elif user_input == "1":
            print("나도 이해도 안 가는 감정 대신 객관적인 장르가 최고라 생각해.")
        elif user_input == "2":
            print("좋아. 다시 감정에 충실해 보자고.")
        elif user_input == "3":
            print("그래. 다시 처음으로.")
            return
        else:
            print("그래, 나도 좀 쉬자고")
            break

def second():
    while True:
        user_input = input("그래, 여기도 길이야. ")

        
        if user_input == "0":
            print("인상적인 선택인데?")
        elif user_input == "1":
            print(".")
        elif user_input == "2":
            print("그래, 다시 돌고 돌아 거기.")
            return
        else:
            print("너가 이겼어. 할 말이 다 떨어졌다고.")
            break

if __name__ == "__main__":
    main_menu()
