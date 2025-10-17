# 더하기 빼기 곱하기 나누기 제곱을 입력 받기
# 숫자 두개를 입력 받기
# 함수 하나에 '연산종류' '숫자 두개' 넣어서 결과 출력하기
# (0으로 나눌 수 없음, 이 경우 따로 케어해야 한다.)

def call(ca, a, b):
    if ca == '1':
        return a + b
    elif ca == '2':
        return a - b
    elif ca == '3':
        return a * b
    elif ca == '4':
        if b == 0:
            return "0으로 나눌 수 없음."
        return a / b
    elif ca == '5':
        return a ** b
    else:
        return "지원하지 않는 연산"
    
ca = input("입력(1.+, 2.-,3.*,4./,5.**)")
a = float(input("첫번째: "))
b = float(input("두번째: "))

result = call(ca, a, b)
print("결과: ", result)

