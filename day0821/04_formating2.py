# 포맷 함수를 사용한 포매팅

print()
print("I eat {0} apples.".format(3))
print()
print("I eat {0} apples.".format("five"))
print()
number = 7
print("I eat {0} apples".format(number))

number = 10
day = "three"

print("I ate {0} apples, so I was sick for {1} days.".format(number, day))

print("I ate {number} apples, so I was sick for {day} days.".format(number=10, day=3))

print("I ate {0} apples, so I was sick for {day} days.".format(number, day=3))

print()
print("-----포매팅과 정렬1-----")
print()
print("{0:<10}".format("hi"))
print()
print("{0:>10}".format("hi"))
print()
print("{0:^10}".format("hi"))
print()
print("{0:=^10}".format("hi"))
print()
print("{0:!<10}".format("hi"))
print()
y=3.141592
print("{0}".format(y))
print("{0:0.3f}".format(y))
print("{0:10.3f}".format(y))

print()
print("-----포매팅과 정렬2-----")

name = '홍단무'
age = 20
print(f'나의 이름은 {name}입니다. 나이는 {age} 입니다.')
print()
print(f'나는 내년이면 {age + 1}살이 됩니다.')
print()
# 딕셔너리 {키:벨류}

d = {'name':'홍단무','age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print()

print(f'{"hi":<10} a')
print(f'{"hi":>10} a')
print(f'{"hi":^10} a')
print(f'{"hi":=^10} a')
print(f'{"hi":!>10} a')
print()
y = 3.141592
print(f'{y:0.4f} a')
print(f'{y:10.4f} a')
print()

print('난 2000000000원이 필요해')
print(f' 난 {2000000000:,}원이 필요해')

# 문자열 포매팅

# 1번
print(f'{"***":>6}cat****')

# 2번
pi = 3.141592
print(f'{pi:>10}_____')
print(f'{"":3}__{pi:.2f}')


# 3번
# 00042 (5칸 확보하고 나서 0으로 채우기)
num = 42
print(f'{num:05}')

# 4번
a = 7.3
# __7.30 (10칸 확보하고 소수점 아래 두자리로)
print(f'{a:_>10.2f}')
