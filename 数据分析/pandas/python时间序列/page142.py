import numpy as np
import pandas as pd

# 显示所有列
pd.set_option("display.max_columns", None)

file_path = "D:\\BaiduNetdiskDownload\\911.csv"

df = pd.read_csv(file_path)
# print(df.head(10))
# print(df.info())

temp_list = df["title"].str.split(":").to_list()

cate_list = list(set([i[0] for i in temp_list]))

zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
# 一种方法
# for cate in cate_list:
# 	zeros_df[cate][df["title"].str.contains(cate)] = 1
#
# 第二种方法
for i in range(zeros_df.shape[0]):
	zeros_df.loc[i, temp_list[i]] = 1


print(zeros_df)
