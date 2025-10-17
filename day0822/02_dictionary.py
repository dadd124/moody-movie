# 딕셔너리 관련 함수
a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print("---키값 뽑아보기---")
print(a.keys())

for k in a.keys():
    print(k)

b = list(a.keys()) # 리스트로 변환
print(b)

print()
print("---벨류값 뽑아보기---")

print(a.values())
c = list(a.values())
print(c)

print()
print("---키, 벨류값 뽑아보기---")
print(a.items())
d = list(a.items())
print(d)

print()
print("---벨류 지우기---")

print()
print("--get--")
a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a['name'])
print(a['phone'])
print(a['birth'])

print()
print("--pop--")

