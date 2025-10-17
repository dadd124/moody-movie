import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.width', 500)

# ------------------------------------------------------------------

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

# ------------------------------------------------------------------

# plt.plot(sr_one)
# plt.show()
# plt.plot(sr_one.index, sr_one.values)
# plt.show()

plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()

# ------------------------------------------------------------------

plt.figure(figsize=(14, 7))
plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
plt.xticks(rotation=90)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'])
plt.show()

print(sr_one.index)

# -----------------------------------------------------------------

plt.figure(figsize=(14, 5))
plt.plot(sr_one.index, sr_one.values,
         marker='o',
         markerfacecolor='red',
         markeredgecolor='blue',
         markeredgewidth=2,
         markersize=10,
         label='서울 -> 경기')

# 엑스틱스로 로테이션 90
# 타이틀 '서울 -> 경기 인구 이동'
# 엑스축라벨 '기간'
# 와이축라벨 '이동인구수'
# 범례 폰트사이즈 15

plt.title('서울 -> 경기 인구 이동', size=20)
plt.xticks(rotation=90, size=10)
plt.xlabel('기간', size=15)
plt.ylabel('이동인구수', size=15)
plt.legend()
plt.show()