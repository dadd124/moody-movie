

head = "Python"
tail = "is fun!"
print()
print(head + tail)

print()
a= "Python"
print(a * 2)

print()
print("=" * 50)
print("My Program")
print("=" * 50)

print("--문자열 길이 구하기--")
print()
a = "Life is too short"
print(len(a))

print()
print("--문자열 인덱싱--")
a = "Life is too short, You need Python"
print("a[3] =", a[3]) #e
print("a[0] =", a[0]) #L
print("a[-1] = ", a[-1]) #n
print(a[-2]) #o
print(a[-5]) #y

print()
print("--문자열 슬라이싱--")
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a = "Life is too short, You need Python"
b = a[0:4]
print(b) #Life

b = a[0:3] # 0 <= a < 3
print(b) #Lif

b = a[0:5]
print(b) #'Life ' Life 다음 자리가 빈 칸이라 공백을 뽑은 것

b = a[5:7]
print(b) # is
b = a[12:17]
print(b) #short
b = a[19:]
print(b) # You need Python

# Life is too short
b = a[0:17]
print(b)

b = a[:]
print(b)

b = a[19:-7]
print(b)

print()
print("------문자열 나누기------")
a = "20250821Suuny"
date = a[0:8]
weather = a[8: ]
print("오늘 날짜 = ", date)
print("오늘 날씨 = ", weather)

a = "20250821Suuny"
year = a[:4]
date = a[4:8]
weather = a[8:]
print("올해 년도 = ", year)
print("오늘 날짜 = ", date)
print("오늘 날씨 = ", weather)

print()
print("-" * 10)
print()

a = "Pithon"
print(a[:1] + 'y' + a[2:])
# Python