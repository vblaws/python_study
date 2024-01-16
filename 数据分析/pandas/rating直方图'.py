import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.head(1))
rating_data = df["Rating"].values
print(type(rating_data))
rating_max = int(rating_data.max())
rating_min = int(rating_data.min())
# print(rating_max - rating_min)
# 计算组数
d = 1
bin_num = int((rating_max - rating_min) // d)

plt.figure(figsize=(20, 8), dpi=80)

plt.hist(rating_data, bin_num)
plt.xticks(range(rating_min, rating_max + d, d))
plt.savefig("D:\\matplotlib可视化图\\rating直方图.png")
plt.show()
