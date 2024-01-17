import numpy as np
import pandas as pd

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
# print(df.head())
# Genre表示类型的意思
temp_list = df["Genre"].str.split(",").tolist()

genre_data = list(set([i for j in temp_list for i in j]))  # 先转换为集合去重,然后转换为列表
print(type(genre_data))
# print(len(set(genre_data)))

# 构造全为0的数组

df = pd.DataFrame(np.zeros((df.shape[0], len(genre_data))), columns=genre_data)
print(df)
