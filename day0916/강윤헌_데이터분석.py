import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('./data/ISSUE_HW_DAY_2019-05_2019-05_2021.xls.xlsx')
dp = pd.read_excel('./data/ISSUE_HW_DAY_2025-05_2025-05_2025.xls.xlsx')

df.info()
print()
dp.info()
print()

df1 = df[df.astype(str).apply(lambda row: row.str.contains('인천').any(), axis=1)]

df1.info()

df1['날짜'] = pd.to_datetime(df1['일시'], errors='coerce')
dp['날짜']  = pd.to_datetime(dp['일시'], errors='coerce')

df1['월일'] = df1['날짜'].dt.strftime('%m-%d')
dp['월일']  = dp['날짜'].dt.strftime('%m-%d')

df_group = df1.groupby('월일')['평균기온'].mean()
dp_group = dp.groupby('월일')['평균기온'].mean()

print(df_group)
print()
print(dp_group)
print()

df_group_max = df1.groupby('월일')['최고기온'].mean()
dp_group_max = dp.groupby('월일')['최고기온'].mean()

print()

plt.figure(figsize=(14,6))

df_group = df1.groupby('월일')['평균기온'].mean()
df_group = df_group.rolling(window=3, center=True).mean() 

dp_sorted = dp.sort_values('월일')
dp_temp = dp_sorted['평균기온'].rolling(window=3, center=True).mean()

plt.plot(df_group.index, df_group.values, 
         label='2019~2021 평균', color='blue', linewidth=2)

plt.plot(dp_sorted['월일'], dp_temp, 
         label='2025', color='orange', linewidth=2)

plt.title('인천 기온 비교 (2019~2021 vs 2025)', fontsize=16)
plt.xlabel('월-일', fontsize=12)
plt.ylabel('기온(℃)', fontsize=12)

plt.xticks(range(0, len(df_group.index), 2), df_group.index[::2], rotation=45)

plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14,6))

df_group_max_smooth = df_group_max.rolling(window=3, center=True).mean()
dp_group_max_smooth = dp_group_max.rolling(window=3, center=True).mean()

plt.plot(df_group_max_smooth.index, df_group_max_smooth.values, 
         label='2019~2021 최고기온 평균', color='blue', linewidth=2)

plt.plot(dp_group_max_smooth.index, dp_group_max_smooth.values, 
         label='2025 최고기온', color='red', linewidth=2)

plt.title('인천 최고기온 비교 (2019~2021 vs 2025)', fontsize=16)
plt.xlabel('월-일', fontsize=12)
plt.ylabel('최고기온(℃)', fontsize=12)

plt.xticks(range(0, len(df_group_max.index), 2), df_group_max.index[::2], rotation=45)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()