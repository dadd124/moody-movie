import json
import os

filename = "hotel.json"

# 초기 데이터
hotel = {
    "1층": {"101": "---", "102": "---", "103": "---"},
    "2층": {"201": "---", "202": "---", "203": "---"},
    "3층": {"301": "---", "302": "---", "303": "---"}
}

# 파일이 없으면 초기 데이터 저장
if not os.path.exists(filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(hotel, f, ensure_ascii=False, indent=4)

# 파일에서 데이터 불러오기
with open(filename, "r", encoding='utf-8') as f:
    hotel = json.load(f)

print(hotel)

while True:
    print("\n[1]조회 [2]입실 [3]퇴실 [4]종료")
    num = input("번호입력: ")

    if num == '1':
        for floor, rooms in hotel.items():
            print(f"{floor}:")
            for room_num, occupant in rooms.items():
                print(f" {room_num}: {occupant}")


    elif num == '2':
        room_num = input("호실입력: ") # 203
        floor = room_num[0] + "층"
        if floor in hotel and room_num in hotel[floor]:
            if hotel[floor][room_num] == '---':
                name = input("이름 입력: ")
                hotel[floor][room_num] = name
                print("입실 완료 하였습니다.")
            else:
                print("이미 입실 중인 방입니다.")
        else:
            print("호실을 잘못 입력하셨습니다.")


    elif num == '3':
        room_num = input("호실입력: ")
        floor = room_num[0] + "층"
        if floor in hotel and room_num in hotel[floor]:
            if hotel[floor][room_num] != '---':
                hotel[floor][room_num] = '---'
                print("퇴실 완료 하였습니다.")
            else:
                print("빈 방입니다.")
        else:
            print("호실을 잘못 입력하셨습니다.")

            
    elif num == '4':
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(hotel, f, ensure_ascii=False, indent=4)
        print("저장 후 종료합니다.")
        break
    else:
        print("번호를 잘못 입력하셨습니다.")
