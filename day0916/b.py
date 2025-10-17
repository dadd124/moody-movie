import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', None)

df = pd.read_excel('./data/ISSUE_HW_DAY_2019-05_2019-05_2021.xls.xlsx')
dp = pd.read_excel('./data/ISSUE_HW_DAY_2025-05_2025-05_2025.xls.xlsx')

print(df.head(1))

df1 = df[df.astype(str).apply(lambda row: row.str.contains('인천').any(), axis=1)]

df1['날짜'] = pd.to_datetime(df1['일시'], errors='coerce')
dp['날짜']  = pd.to_datetime(dp['일시'], errors='coerce')

df1['월일'] = df1['날짜'].dt.strftime('%m-%d')
dp['월일']  = dp['날짜'].dt.strftime('%m-%d')

df['날짜'] = pd.to_datetime(df['일시']).dt.year
heat_days = df.groupby('날짜')['지점 폭염여부'].apply(lambda x: (x=='O').sum())
print(heat_days)