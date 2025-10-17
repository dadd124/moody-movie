import pandas as pd
import numpy as np

pd.set_option('display.unicode.east_asian_width', True)

df = pd.read_excel('./data/주가데이터.xlsx')
# print(df)
print()
print(df.head(2))
print()
print(df.head(1).info())
print()
print(df.columns)
print()
df = df.rename(columns={'시가':'사가','저가':'저기'})
print(df.head(1))
print()

# 컬럼 삭제
df1 = df.drop('저기', axis=1)
print(df.head(1))

df2 = df.drop(['사가', '저기'], axis=1)
print(df2.head(1))
print()

# 로우(행) 삭제

df3 = df.drop(0)
print(df3.head(2))
print()

# loc, iloc
print(df.head(1))
print()

# df.loc[행  , 열  ]
# df.iloc[ 행  , 열  ]

# 인덱스 이름으로 동작
df1 = df.loc[1:4, '사가':'저기'] # 여긴 1부터 4까지
print(df1)
print()

# 정수 인덱스로 동작
df2 = df.iloc[1:5, 1:4] # 여긴 1:5는 1부터 4까지 0부터 시작임
print(df2)
print()

# 컬럼 선택
df3 = df.loc[:,['사가', '연월일', '거래량']] # 뽑으면서 새로 만듦
print(df3.head(3))
print()

df4 = df.loc[:, '사가']
print(df4)

df5 = df.loc[1, :]
print(df5)
print()

# 컬럼 선택2
df1 = df['사가']
print(df1)
print()

df2 = df[['사가', '저기', '연월일']]
print(df2)

# df.loc[ 행, 열 ]
# df[[컬럼들]]

df3 = df.loc[3, '사가']
print(df3)
print(type(df3))
print()

df4 = df.loc[3, ['사가']]
print(df4)
print(type(df4))
print()

df5 = df.loc[3:3, ['사가']]
print(df5)
print(type(df5))
print()

print(df)
print()

# 정렬하기
ndf = df.sort_values(by='사가')
print(ndf)
print()

ndf = df.sort_values(by='사가', ascending=False)
print(ndf)
print()

# 새로운 컬럼
df['십년뒤'] = df['사가'] + 10
print(df)
print()

# 필터링
print(df['십년뒤'] < 12000) # 불리언 시리즈

# df[  불리언 시리즈  ]

df1 = df[df['십년뒤'] < 12000]
print(df1)

# 십년뒤 12000 미만, 전일종가 == 100
filter = (df['십년뒤'] < 12000) & (df['전일종가'] == 0)
print(filter) # 불리언 시리즈
print()

df2 = df[filter]
print(df2)
print()

# 조회 2

print(df.shape)
print()
print(df.ndim)
print()
print(df.describe(include='all'))
print()

# 평균값

d_mean = df['사가'].mean()
print('사가 평균: ', d_mean )

# mean, medianb, max, min, std
# corr

print(df[['사가', '저기']].corr())
print()

# 널 값

df.loc[5:6, '사가'] = np.nan
print(df)
print()

df.info()
print()

df.info()
print()
print(df['사가'].value_counts(dropna=False))
print()
print(df.isnull().sum())
print()

df['사가'] = df['사가'].fillna(d_mean.round()).astype(int)
df.info()
print()
print(df)
print()

df['사가_S'] = (df['사가'] - df['사가'].min()) / (df['사가'].max() - df['사가'].min())
print(df)

def min_max(col):
    return(col - col.min()) / (col.max() - col.min())

df_n = df[['사가', '십년뒤']]
print(df_n)
print()

scaled = df_n.apply(min_max)
print(scaled)

# map, apply, pipe
# groupby
# concat, merge, pivot

# pclass 별 평균값으로 채우기
# 널값 데체를 다양한 방식으로 하고 데이터 분석 마무리

