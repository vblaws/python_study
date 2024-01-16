import pandas as pd
from matplotlib import pyplot as plt

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.info())


runtime = df["Runtime (Minutes)"].values
print(type(runtime))
print(runtime.shape)
# print(runtime)
runtime_max = runtime.max()
runtime_min = runtime.min()

# 计算组数
d = 5
num_bin = (runtime_max - runtime_min) // d
# 绘制直方图
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime, num_bin)
plt.xticks(range(runtime_min, runtime_max + d, d))
plt.savefig("D:\\matplotlib可视化图\\电影数据直方图.png")
plt.show()
awdawdwad