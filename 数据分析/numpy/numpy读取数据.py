import numpy as np

us_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\US_video_data_numbers.csv"
gb_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\GB_video_data_numbers.csv"

# t1=np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=False)
# print(t1)
# print("*"*100)
print(t2)

# t2取行
print(t2[2])
# 取连续的多行
print(t2[2:])
# t3=np.arange(24).reshape((2,12,))
# print(t3[1:])
# 取不连续的多行
print(t2[[2, 12, 13]])
# 取列
print(t2[:, 1:])
# 例子:第一列，所有行
print(t2[:, 0])
# 列子：从第二行开始，取不规则的列
print("-" * 100)
print(t2[2:, [0, 1, 3]])
print("-" * 100)
# 取行和列
print(t2[2, 3])
print("-" * 100)
# 取多行多列
print(t2[2:5, 1:4])
print("-" * 100)
# 取多个不相邻的点
print(t2[[1, 2], [3, 1]])

t3 = np.arange(24).reshape((4, 6,))
t3[t3 < 10] = 3
t3[t3 > 20] = 20
print(t3)
print("^" * 100)
t4 = np.arange(24).reshape((4, 6,))
print(t4)
t4 = np.where(t4 < 10, 0, 10)
print(t4)
print("$" * 100)

t5 = np.arange(24).reshape((4, 6,))

t5 = t5.astype(float)
t5[3, 3] = np.nan

print(t5)