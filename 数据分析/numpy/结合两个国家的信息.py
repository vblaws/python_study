import numpy as np

us_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\US_video_data_numbers.csv"
gb_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\GB_video_data_numbers.csv"

us_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")
uk_data = np.loadtxt(gb_file_path, delimiter=",", dtype="int")

# print(t1)
# print(t2)
# print("拼接之后的数据")
# print(np.vstack((t1, t2)))
# print(us_data)
# print(uk_data)
print("*" * 100)
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)
# 水平拼接
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))
# 竖直拼接
final_data = np.vstack((us_data, uk_data))
print(final_data)