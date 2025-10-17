import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#음수표기
plt.rcParams['axes.unicode_minus'] = False
#터미널 넓이
pd.set_option('display.width', 500)

# --------------------------------------------

df = pd.read_excel('data/시도별_전출입_인구수.xlsx')

print(df.head())
print()

df = df.ffill()
print(df.head())
print()

# 전출지 = 서울, 전입지 = 서울빼고 ---> 서울을 나간 사람들 (네튤농 - 순정)

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop('전출지별', axis=1)
df_seoul = df_seoul.rename({'전입지별':'전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')
print(df_seoul)
print()

sr_one = df_seoul.loc['경기도']
print(sr_one)
print()

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
print(df_4)
df_4 = df_4.T

# 스타일 지정
plt.style.use('ggplot')

# 막대 그래프 그리기
df_4.plot(kind='bar', figsize=(10, 5), width=0.5,
          color=['orange', 'green', 'skyblue', 'blue'])

plt.title('서울 -> 타도시 인구 이동', size=25)
plt.ylabel('이동 인구수', labelpad=7, size=15)
plt.xlabel('기간', labelpad=7, size=15)
plt.ylim(5000, 30000)
plt.tick_params(axis='x', rotation=0)
plt.legend(fontsize=10)
plt.show()

# ------------------ 가로형 막대 그래프 ---------------------

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
print(df_4)
print()

df_4['합계'] = df_4.sum(axis=1)
print(df_4)
print()

df_total = df_4[['합계']].sort_values(by='합계', ascending=True)
print(df_total)

df_total.plot(kind='barh', figsize=(10,5))
plt.show()

