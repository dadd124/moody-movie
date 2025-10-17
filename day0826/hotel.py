import os

FILENAME = "hotel.txt"

def load_rooms():
    rooms = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                room, guest = line.strip().split(",")
                rooms[room] = guest if guest != "빈방" else None



def check_in(rooms):
    room = input("원하시는 방 번호를 입력: ")
    if room not in rooms:
        print("존재하지 않는 방입니다.")
        return
    if rooms[room]:
        print("사용 중인 방입니다.")
        return
    name = input("성함: ")
    rooms[room] = name
    print(f'{room}호에 {name}님 입실하셨습니다.')

def check_out(rooms):
    room = input("머물렀던 방 번호를 입력: ")
    if room not in rooms:
        print("존재하지 않는 방입니다.")
        return
    if not rooms[room]:
        print("이미 빈 방입니다.")
        return
    print(f"{room}호 퇴실 완료.")
    rooms[room] = None





