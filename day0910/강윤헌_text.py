import pandas as pd
import seaborn as sns
import numbers as np

# 1.  Seaborn의 titanic 데이터셋을 불러와 titanic 변수에 저장하시오.
Titanic = sns.load_dataset('titanic')

# 2.  Titanic 데이터의 기본 정보를 조회하시오
Titanic.info()

# 3.  Titanic 데이터의 행과 열 개수를 조회하고, 몇 차원 배열인지 조회하시오
print(Titanic.shape)
print(Titanic.ndim)

# 4.  첫 3행과 마지막 2행을 조회하시오
print(Titanic.head(3))
print(Titanic.tail(2))

# 5.  loc을 사용해 첫 5행에서 열 ['survived','pclass','sex','age']만을 가진 데이터프레임 df_loc을 만들고, 출력하시오.
df_loc = Titanic.loc[:4, ['survived','pclass','sex','age']]
print(df_loc)
print()

# 6.  iloc을 사용해 행 10~14(포함), 열 0~3(포함)을 추출해 df_iloc에 저장하고, 출력하시오.
df_iloc = Titanic.iloc[10:15, 0:4]
print(df_iloc)
print()

# 7.  원본을 훼손하지 않고(inplace=False) titanic에서 열 ['deck','embark_town']을 드랍한 새 데이터프레임 df_drop_cols를 만드시오.
df_drop_cols = Titanic.drop(['deck','embark_town'], axis=1)
print(df_drop_cols.shape)
print()

# 8.  결측치가 하나라도 있는 행을 드랍한 데이터프레임 df_dropna_rows를 만드시오.
df_dropna_rows = Titanic.dropna()
print(df_dropna_rows.shape)
print()

# 9.  각 열별 결측치 개수를 Series로 구하시오.
print(Titanic.isna().sum())
print()
# 10.  age 열의 결측치 개수만 따로 출력하시오.
print(Titanic['age'].isna().sum())
print()

# 11.  age 열의 평균값으로 해당 열의 결측치를 대체한 새로운 시리즈 age_filled를 만드시오(원본 불변).
age_mean = Titanic['age'].mean()
age_filled = Titanic['age'].fillna(age_mean)
print("age_filled 생성 완료")
print()

# 12.  대체 전후 age의 결측치 개수를 각각 출력하여 비교하시오.
print(Titanic['age'].isna().sum())
print(age_filled.isna().sum())
print()

# 13.  embarked 열의 최빈값을 describe() 결과로 확인하시오.
print(Titanic['embarked'].describe())
mode_embarked = Titanic['embarked'].mode()[0]
print(mode_embarked)
print()

# 14.  그 최빈값으로 embarked의 결측치를 대체한 embarked_filled 시리즈를 만드시오(원본 불변).
embarked_filled = Titanic['embarked'].fillna(mode_embarked)
print(embarked_filled.isna().sum())
print()

# 15.  수치형 열 중 ['age','fare']만 선택하여 0~1 범위로 Min-Max 스케일링한 데이터프레임 df_scaled를 만드시오(사전 결측 대체 필요 시 적절히 처리).
df_num = Titanic[['age','fare']].copy()
df_num['age'] = df_num['age'].fillna(df_num['age'].mean())
df_num['fare'] = df_num['fare'].fillna(df_num['fare'].mean())

df_scaled = (df_num - df_num.min()) / (df_num.max() - df_num.min())
print(df_scaled.head())
print()

# 16.  스케일링 후 각 열의 최소/최대가 0과 1에 가깝게 되었는지 describe()로 확인하시오.
print(df_scaled.describe())
print()

# 17.  age를 기준으로 아동(018], 성인(18100]) 4구간으로 나누어 새 열 age_bin 을 생성하시오.
bins = [0, 12, 18, 60, 100]
labels = ['아동','청소년','성인','노인']
Titanic['age_bin'] = pd.cut(Titanic['age'], bins=bins, labels=labels, right=False)  
print("age_bin 생성 완료")
print(Titanic[['age','age_bin']].head(15))
print()

# 18.  각 구간별 인원수를 구하시오.
print(Titanic['age_bin'].value_counts())
print()

# 19.  pclass와 sex로 그룹화하여 survived의 평균 생존율을 구하시오.
survival_rate = Titanic.groupby(['pclass','sex'])['survived'].mean()
print(survival_rate)
print()

# 20.  위 결과를 생존율 내림차순으로 정렬하시오.
print(survival_rate.sort_values(ascending=False))
print()

# 21.  age_bin(문항17)과 sex로 그룹화하여 fare의 중앙값을 구하시오.
fare_median = Titanic.groupby(['age_bin','sex'])['fare'].median()
print("fare 중앙값:\n", fare_median)
