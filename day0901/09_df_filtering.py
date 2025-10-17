import pandas as pd
import seaborn as sns
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.head())
titanic.info()

# age fare 컬럼... 0~9 행, 데이터 뽑아보기
df = titanic.loc[0:9, ['age','fare']]
print(df)
print()

print("---- 데이터 필터링 ----")
print()

print(df['age'])
print()
print(df['age'] < 20)
print()
print(df[df['age'] < 20]) # *****
print()
print(df.loc[df['age'] < 20])
print()

print("---- 논리연산자 ----")
print()

print(df.loc[~(df['age'] < 20)])

# df말고 titanic 해서 head만 뽑아보기. 10 살 이상 & 20살 미만

print(titanic[titanic['age'] >= 10 & (titanic['age'] < 20 )].head())

mask1 = (titanic['age'] >= 10) & (titanic['age'] < 20)
print(mask1)
print(type(mask1))
print()

df_teenage = titanic[mask1]
print(df_teenage.head())
print()

mask2 = (titanic['age'] < 10) & (titanic['sex'] == 'female')
df_female_under10 = titanic[mask2]
print(df_female_under10.head())
print()

print("---- 행 컨디션 열 셀렉션 ----")
print()

df_female_under10 = titanic.loc[mask2, ['age', 'sex']]
print(df_female_under10.head())
print()

mask3 = titanic['age'] >= 20
print(mask3.head())
print()

print(mask3)
print()

titanic['df_y_o'] = mask3
print(titanic.head())

# ----------------------------------------------

mask1 = titanic['embark_town'] == "Southaampton"
mask2 = titanic['embark_town'] == "Queenstown"
df_boolean = titanic[mask1 | mask2]
print(df_boolean.head())
print()