import re

print("--- 영어 단어만 추출 ---")

text = "Python 정규식, Hello world! 123"
pattern = "[a-zA-Z]+"

words = re.findall(pattern, text)
print("영어 단어: ", words)

print("--- 숫자만 추출 ---")

text = '오늘은 2025년 8월 29일, 수업은 3시간'
# pattern = "[0-9]+"
pattern = "\d+"

numbers = re.findall(pattern, text)
print('숫자 추출: ', numbers)

print("--- 특정 단어로 시작하는 단어 찾기 ---")

text = "cat scatter cater catalog dog"
pattern = r"\bcat\w*"

matches = re.findall(pattern, text)
print("cat으로 시작하는 단어: ", matches)
print()

print("--- or ---")

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
print()

print("--- 문자열 바꾸기---")
print()

p = re.compile('blue|white|red')
m = p.sub('color', 'blue socks and red shoes')
print(m)
print()

print("--- 모든 공백을 하나로 줄이기 ---")
print()

text = '안녕하세요   반갑습니다\t 저는   파이썬을 공부해요'
pattern = r"\s+"

result = re.sub(pattern ," ", text)
print("공백 정리: ", result)

print("--- 간단한 URL 찾기 ---")
print()

text = "사이트: http://example.com, 보안:https://secure.org/path"
pattern = r"https?://\S+"
# pattern = r"https?://[A-Za-z0-9./-]"

urls = re.findall(pattern, text)
print("URL 추출:", urls)
# URL 추츨: ['http://example.com,', 'https://secure.org/path']
print()

print("--- 이메일 추출 ---")
print()

text = """
문의: cs@text.co / backup: me.example+dev@sub-domain.example.com
스팸: a@b, user@.com, 정상: hello.world@domain.io
"""

pattern = r"[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print("이메일 추출: ", emails)
['cs@test.co', 'me.example+dev@sub-domain.example.com', 'hello.world@domain.io']

print("----- ^ $ -----")
print()
# ^Hello ==> 문장이 ^Hello 로 시작해야 함
m = re.match(r"^Hello", "Hellow world")
m2 = re.match(r"^Hello", "well, Hello")

m3 = re.search(r"^a", "apple")
m4 = re.search(r"^a", "banana")

print(m)
print(m2)
print(m3)
print(m4)

# ^Hello ==> 문장이 ^Hello 로 끝나야 함
m = re.search('short%', 'Life in too short')
print(m)

m2 = re.search('short$', 'Life is too short, you need python')
print(m2)