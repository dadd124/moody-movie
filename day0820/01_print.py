print("--------------")
print()
print("첫 프린트입니다.")
print('작은 따옴표')
print()
print("-------------")

food = "Python's favorite food is perl"

print(food)
# food = 'Python's favorite food is perl'

say = '"Python is very easy." he says.'
print(say)

food = 'Python\'s favorite food is perl'
print(food)

say = "\"Pyton is very easy.\" he says."
print(say)

print("--여러 줄 작상--")
multiline='''
Life is too short
You need python
'''

print(multiline)

multiline="""
Life is too short
You need python
"""
print(multiline)

multiline = "Life is too short\nYou need python"
print(multiline)

print()
print("--이스케이프 코드--")
# 자주 사용하는 코드 -- \n \' \" \t \\ 

a = "a\n s"
print(a)

b = "a\'s"
print(b)

c = "a\"s"
print(c)

d = "a\ts"
print(d)

f = "a\\s"
print(f)

slamdunk = '''
강백호\t\t\\덩크\t\\33
통키\t\t\\불꽃슛\t\\100
세일러문\t\\변신\t\\7
'''
print(slamdunk)