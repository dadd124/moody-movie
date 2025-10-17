import re

print("----- DOTALL -----")
print()

p = re.compile('a.b')
m = p.match('a\nb') # 라인개행 만큼은 못찾음
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb') # 라인개행까지 포함해서 매치
print(m)

print("----- IGNORECASE -----")
print()

p = re.compile('[a-z]+', re.I)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
m = p.match('PYTHON')
print(m)

print("----- MULTILINE -----")
print()

p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

m = p.findall(data)
print(m)

print("---- 문장의 첫 단어 추출 (멀티라인) ----")

text = """Hello world
안녕하세요 파이썬
@@@ 골뱅이
 공백 시작
_언더 시작
Regex is powerful"""

pattern = r"^\w+"

p = re.compile(pattern, re.M)
m = p.findall(text)
print(m)