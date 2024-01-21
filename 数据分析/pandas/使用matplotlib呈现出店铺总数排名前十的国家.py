import pandas as pd
from matplotlib import pyplot as plt
# 设置显示所有的列,
pd.set_option("display.max_columns", None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\starbucks_store_worldwide.csv"

data = pd.read_csv(file_path)
# 使用matplotlib呈现出店铺总数排名前十的国家
# 准备数据
df = data.groupby(by=data["Country"])["Brand"].count().sort_values(ascending=False)[:10]
# print(type(df))
_x = df.index
_y = df.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(_x,_y)

plt.show()