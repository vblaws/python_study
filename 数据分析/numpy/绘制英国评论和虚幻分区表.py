import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
gb_file_path = "D:\\EageDownload\\DataAnalysis-master\\day03\\code\\youtube_video_data\\GB_video_data_numbers.csv"

t_uk = np.loadtxt(gb_file_path, delimiter=",", dtype="int")
t_uk = t_uk[t_uk[:, 1] < 500000]

# 这段代码是Python代码，它对一个名为t_uk的二维数组（或称为表格、矩阵）进行操作。具体来说，它筛选出t_uk中所有第二列（索引为1）的值大于500,000的行。
#
# 让我们逐步解释这段代码：
#
# t_uk[:, 1]: 这部分代码选择了t_uk数组的所有行（:表示所有行）和第二列（索引为1）。
# t_uk[:, 1] > 500000: 这部分代码对上一步选出的第二列中的每个值进行了比较，看它是否大于500,000。结果是一个布尔数组，其中每个元素都是True或False，表示相应的比较结果。
# t_uk[t_uk[:, 1] > 500000]: 这部分代码使用上一步得到的布尔数组来索引t_uk。只有那些第二列值大于500,000的行会被选中。
# 最终，t_uk数组中所有第二列值大于500,000的行都会被保留，而其他行都会被删除。

t_uk_comment = t_uk[:, -1]
t_uk_like = t_uk[:, 1]
# print(t_uk_comment)
# print(t_uk_like)
plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(t_uk_like, t_uk_comment)
plt.savefig("D:\\matplotlib可视化图\\comment_like.png")
plt.show()
