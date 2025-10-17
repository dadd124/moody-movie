import os
FILENAME = "./day0827/rooms.txt"

def load_rooms():
    rooms = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                room, guest = line.strip().split(",")
                rooms[room] = guest if guest != "빈방" else None
    else:

        for floor in range(1, 4):
            for num in range(1, 4):
                rooms[f"{floor}0{num}"] = None
    return rooms

def save_rooms(rooms):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for room, guest in rooms.items():
            f.write(f"{room},{guest if guest else '빈방'}\n")

def show_rooms(rooms):
    print("\n=== 객실 현황 ===")
    for floor in range(1, 4):
        for num in range(1, 4):
            room = f"{floor}0{num}"
            guest = rooms[room] if rooms[room] else "빈방"
            print(f"{room}: {guest}", end="   ")
        print()
    print()

def check_in(rooms):
    room = input("입실할 방 번호(예: 101): ")
    if room not in rooms:
        print("존재하지 않는 방입니다.")
        return
    if rooms[room]:
        print("이미 사용 중인 방입니다.")
        return
    name = input("투숙객 이름: ")
    rooms[room] = name
    print(f"{room}호에 {name}님 입실 완료.")

def check_out(rooms):
    room = input("퇴실할 방 번호(예: 101): ")
    if room not in rooms:
        print("존재하지 않는 방입니다.")
        return
    if not rooms[room]:
        print("이미 빈 방입니다.")
        return
    print(f"{room}호 {rooms[room]}님 퇴실 완료.")
    rooms[room] = None

def main():
    rooms = load_rooms()
    while True:
        print("\n1. 조회  2. 입실  3. 퇴실  4. 종료")
        choice = input("선택: ")
        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            check_in(rooms)
            save_rooms(rooms)
        elif choice == "3":
            check_out(rooms)
            save_rooms(rooms)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            save_rooms(rooms)
            break
        else:
            print("잘못된 입력입니다. 1~4를 선택하세요.")

if __name__ == "__main__":
    main()