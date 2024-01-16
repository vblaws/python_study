import numpy as np
import pandas as pd

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
print(df)

print(df.info())
print(df.isnull())
print(df.head(1))

print("-" * 120)
# 获取电影平均评分
print(f"平均评分{df["Rating"].mean()}")
# 获取导演人数
print(f"导演人数为{len(set(df["Director"].tolist()))}")

temp_actors_list = df["Actors"].str.split(",").tolist()
# print(len(df["Actors"].tolist()))
actors_list = [i for j in temp_actors_list for i in j]
# actors_list = np.array(temp_actors_list).flatten()
# set()方法是为了去除重复值
print(f"演员人数{len(set(actors_list))}")
