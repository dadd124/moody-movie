# !!! 그루핑 !!!
# 1. 여러문자를 하나로 묶어서 반복 처리
# 매치된 문자열에서 원하는 부분만 추출

import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m) # <re.Match object; span = (0, 9), match = 'ABCABCABC'>
print(m.group())

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-5678")

# 이름 부분만 추출하고 싶다면?
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-5678")
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print(m)
print()

print("---- 이메일 사용자명과 도메인 분리 ----")

text = '문의: hello.world@python.org'
pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

match = re.search(pattern, text)
print("전체:", match.group(0))
print("사용자명:", match.group(1))
print("도메인:", match.group(2))

'''
전체: hello.world@python.org
사용자명: hello.world
도메인: python.org
'''

print("--- 중복된 글자 줄이기 ---")
print()

text = "와아아 대박!!! 굿굿굿"
pattern = r"(.)\1{2,}"

result = re.sub(pattern, r"\1\1", text)
print("중복 줄이기:", result)

print("--- 기초 연습 1 ---")
print()

text = "w3ar@aef.com, fail91@e0r9guj.kr, a@a.a"
p = re.compile(r"\w+@\w+\.\w+") # a@a.a
m = p.findall(text)
print(m)
print()

print("--- 전화번호 정규화(하이픈 통일) ---")
# 0으로 시작
# 맨앞이 0포함 2~3자리
# 가운데가 3~4 자리
# 끝이 4 자리

text = "고객센터 02-123-1234, 01012341234, 031.123.1234, 010 1234 1234(대표)"

rx = re.compile(r"\b(0\d{1,2})[-. ]?(\d{3,4})[-. ]?(\d{4})")
# 000-0000-0000
normalized = rx.sub(r"\1-\2-\3", text)
print("정규화:", normalized)

m = rx.finditer(text)
print(m)

for i in m:
    print('원본:', i.group(0), "| 지역:", i.group(1),
          "| 국번회:", i.group(2), "| 가입자:", i.group(3))

# finditer 로 각 그룹 확인
'''
정규화: 고객센터 02-123-4567, 010-1234-000, 010 1234 1234(대표)
원본: 02-123-4567 | 지역: 02 | 국번호: 123 | 가입자: 0000
원본: 031-555-0000 | 지역: 031 | 국번호: 555 | 가입자: 0000
'''