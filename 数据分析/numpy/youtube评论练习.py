import numpy as np
from matplotlib import pyplot as plt

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]

us_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\US_video_data_numbers.csv"
gb_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\GB_video_data_numbers.csv"
plt.figure(figsize=(20, 8), dpi=80)
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=False)
# 取评论数
t_us_comment = t_us[:, -1]

t_us_comment = t_us_comment[t_us_comment < 5000]
# 确定组数
d = 50
bin_num = (t_us_comment.max() - t_us_comment.min()) // d

plt.hist(t_us_comment, bin_num)

plt.savefig("D:\\matplotlib可视化图\\youtbeT.png")

plt.show()
