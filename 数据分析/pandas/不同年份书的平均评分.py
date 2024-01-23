import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\books.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.info())
# 删除年份这一行内有空值的行
df = df[pd.notnull(df["original_publication_year"])]
# 筛选出年份大于0的年份`
df = df[df["original_publication_year"] >= 0.0]
# 求出每一年书的平均评分
average_rating = df.groupby(by="original_publication_year")["average_rating"].mean()

print(average_rating)
# 画图
_x = average_rating.index
_y = average_rating.values
print(_x.min())
print(_x.max())
plt.figure(figsize=(25, 14), dpi=90)
plt.xticks(np.arange(_x.min(), _x.max(), 100),rotation=90)
plt.plot(_x, _y)
plt.show()
