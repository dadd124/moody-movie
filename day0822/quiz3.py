# 중첩 while 문으로 구구단 포스터 뽑기

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} 곱하기 {j}는 {i*j}")
        j += 1
    print()
    i += 1
    