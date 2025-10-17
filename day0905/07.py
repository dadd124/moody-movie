import pandas as pd
import numpy as np

# 전처리
df = pd.read_csv('./data/auto-mpg.csv')

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration','model year', 'origin', 'name']
print(df)

# 누락 데이터 확인

print(df.head().isnull())

# 누락 데이터 처리

df['horsepower'] = df['horsepower'].replace('?', np.nan)
print(df)

# 단위변환

df['horsepower'] = df['horsepower'].astype('float')
print(df)

# 필요없는 컬럼 삭제하기

df = df.drop(columns='nan')
print(df)

# 범주 나눠보기 -> 범주별로 인코딩하기

# 중복행 확인 (및 제거)

# 데이터 스케일링(minmax, standard)
