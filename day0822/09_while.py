coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break

coffee = 10
while False:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        coffee = coffee - 1
        print("계산 완료")
    elif money > 300:
        coffee = coffee - 1
        print("계산 완료, 거스름돈 %d원 받아가세요." % (money-300))
    else:
        print("돈이 부족합니다.")
    if coffee == 0:
        print("커피 없습니다.")
        break

print()
print("----continue----")
# while 문의 맨 처음으로 돌아간다

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 무한루프 탈출은 Ctrl + c 혹은 터미널창 닫기

# i = 0
# while i < 10:
#     print("야")

print()
print("----while else----")

count = 0
while count < 3:
    print(f'카운트: {count}')
    count += 1
else:
    print("while 문이 정상 종료 되었습니다.")

print()
print("---while else2---")

count = 0
while count < 5:
    if count == 2:
        break
    print(f'카운트: {count}')
    count += 1
else:
    print("while 문이 정상 종료 되었습니다.")

print()
print("---중첩 while문---")

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1