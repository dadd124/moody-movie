# 다양한 조건 만들기 elif

pocket = ['paper', 'cellphone']
card = True

# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 둘다 없으면 걸어가라
# or, elif 사용하지 말고 , if 랑 else 만 사용해서 if 문 짜보기

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print()
print("--elif--")

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시 타자")
else:
    print("걸어가라")

print()
print("--연쇄 비교 연산자--")

x = 5

print((1 < x) and (x < 10)) # True
print( 1 < x < 10)
print( 10 <= x <= 20) # False

print()
print("--일반 표현식--")

score = 85
if score >= 60:
    result = "합격"
else :
    result = "불합격"

print(result)

print()
print("--조건부 표현식--")

score = 85
result = "합격" if score >= 60 else "불합격"
print(result)

age = 19
# 18살 이상이면 "성인" 아니면 "미성년"

temperature = 25
# 20 초과이면 "따듯함" 아니면 "추움"

money = 1500
# 1000원 이상이면 "버스" 아니면 "걷자"

result = "성인" if age >= 18 else "미성년"
print(result)

result = "따듯함" if temperature > 20 else "추움"
print(result)

result = "버스" if money >= 1500 else "걷자"
print(result)
