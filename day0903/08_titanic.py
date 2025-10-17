import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 300)


# 타이타닉 로드하기 (사본)
titanic = sns.load_dataset('titanic')
# print(titanic)
print()

# 살아남은 사람이되 나이가 80세 이상인 사람
print(titanic[titanic['age']==80])
print()

print("----- 구분선 -----")

# 데이터 구조 확인
titanic.info()
# print(titanic.head())
print(titanic.tail())
print()

print("----- 구분선 -----")

print(type(titanic))
print()

# 승객의 평균 나이, 요금
df = titanic.loc[:, ['age', 'fare']]
print(df.mean(numeric_only=True))
print()

print("----- 구분선 -----")
df1 = titanic.drop(columns='deck')
print(df1)
print()

print("----- 구분선 -----")
df2 = titanic.loc[:, ['age', 'parch', 'class']]
print(df2)
print()

# FamiliySize 라는 컬럼에 sibsp + parch + 1(자기자신) (로 해서 총 가족 인원수 컬럼 만들어보기)
titanic['FamilySize'] = titanic['sibsp'] + titanic['parch'] + 1
titanic.info()

print("----- 구분선 -----")
# IsChild 라는 True/False 컬럼 만들어보기 (13살 미만)
titanic['IsChild'] = titanic['age'] < 13
titanic.info()
print()
print(titanic['age'] < 13)

print("----- 구분선 -----")
# 불타입 시리즈를 데이터[] 에 넣으면 True에 해당하는 데이터만 필터링

# 남성 여성 평균 나이 비교
print('남자 나이 평균: ', titanic[titanic['sex']=='male']['age'].mean().round(2))
print('여자 나이 평균: ', round(titanic[titanic['sex']=='female']['age'].mean()))

# ti_man = titanic[titanic['sex']=='male']
# ti_man['age'].mean()

# id 라는 이름으로 정수 인덱스 주기
print(titanic)
print()
titanic = titanic.reset_index(names='id')
print(titanic)
print()
