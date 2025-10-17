print()
print("----- pow -----")
print()

print(pow(2,4))
print(pow(3,4))

print()
print("----- range -----")
print()

print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]

print(list(range(1, 10, 2))) # [1, 3, 4, 7, 9]

print(list(range(0, -11, -2))) # [0, -2, -4, -6, -8, -10]
print(list(range(0, -11, -1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, 10] 

print()
print("----- round -----")
print()

print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(4.5)) # 가까운 짝수쪽으로 붙음
print(round(4.51)) # 5

print(round(5.678, 2)) # 5.68

print()
print("----- sorted -----")
print() # 리스트로 반환

print(sorted([3, 1, 2])) # [1, 2, 3]
print(sorted(['a', 'c', 'b'])) # ['a', 'b', 'c']
print(sorted('zero')) # ['e', 'o', 'r', 'z']
print(sorted((3,2,1))) # [1,2,3]

print()
print("----- str -----")
print() # 문자열로 변환

print(str(3))
print(str('hi'))

print()
print("----- range -----")
print()

print(sum([1,2,3])) # 6
print(sum((4,5,6))) # 15

print()
print("----- tuple -----")
print() # 반복 가능한 데이터를 튜플로 반환

print(tuple('abc'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

print()
print("----- type -----")
print()

print(type('abc'))
print(type([]))
print(type(open('text', 'w')))

print()
print("----- zip -----")
print()

print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip('abc', 'def')))

