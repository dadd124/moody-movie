

def main_menu():
    while True:
        print("\n지금 테스트 중이야.")

        user_input = input("\n뭐든 말 좀 해봐: ")
        if user_input == "0":
            first()
        elif user_input == "1":
            second()
        else:
            print("그래, 정리 좀 하고 오라고.")
            break

def first():
    while True:
        user_input = input("그럼 다른 방식으로 알아볼까?")

        if user_input == "0":
            print("장르에 따른 구분이 싫다면 다른 선택지도 있어.")
            second()
        elif user_input == "1":
            print("물론 그 장르도 있지.")
        elif user_input == "2":
            print("좋아. 다시 감정에 충실해 보자고.")
            third()
        elif user_input == "3":
            print("그래. 다시 처음으로.")
            return
        else:
            print("그래, 나도 좀 쉬자고")
            break

def second():
    while True:
        user_input = input("언제나 감정이 뚜렷할 수는 없지. 하지만 좋아하는 배우는 있잖아?")

        
        if user_input == "0":
            print("취향에 따른 선택지도 있지.")
            first()
        elif user_input == "1":
            print("음, 다른 배우도 있어.")
        elif user_input == "2":
            print("그래, 다시 돌고 돌아 거기.")
            return
        else:
            print("너가 이겼어. 할 말이 다 떨어졌다고.")
            break

def third():
    while True:
        user_input = input("다시 돌아온 걸 환영해.")
        if user_input == "0":
            print("그래. 역시 확고한 기준 만한 게 없지.")
            first()
        if user_input == "1":
            print("원래 보고 싶은 사람을 봐야 해")
            second()
        if user_input == "2":
            print("뭐, 새로운 마음으로.")
            return
        else:
            print("음, 생각 정리 좀 하고 있을게.")
            break

if __name__ == "__main__":
    main_menu()