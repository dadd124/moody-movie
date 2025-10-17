import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("./data/auto-mpg.csv", header=None)

# 열 이름 저장
df.columns = ['mpg', 'cylinders', 'dispacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 연비, 실린더수, 배기량, 마력, 차무게, 가속도, 출시연도, 제조국코드, 차이름

print()
print(df.head())
print()
print(df.tail())
print()
print(df.shape())
print()
df.info()
print()
print(df.dtypes)
print()
print(df['mpg'].dtypes) # float64
print()

# -------- 산술 정보 --------

print(df.describe()) # 산술정보
print()
print(df.describe(include='all'))
print()
print(df.describe(include='number')) # 없으면 디폴트 값
print()
print(df.describe(include='obhect'))
print()
print(df.count()) # 유효한 데이터 개수를 시리즈로 변환
print()

unique_values_ratio = df['origin'].value_counts(normalize=True)
print(unique_values_ratio)
print()

unique_values_percentage = (df['origin'].value_counts())
print(unique_values_percentage)