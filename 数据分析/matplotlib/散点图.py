from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]

x_3 = [i for i in range(1, 32)]
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22,
       23]
x_10 = [i for i in range(51, 82)]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12,
        13,
        6]
# 构建画布
plt.figure(figsize=(20, 8), dpi=80)
# 绘制散点图
plt.scatter(x_3, y_3, label='三月')
plt.scatter(x_10, y_10, label='十月')

# 调整x轴文字
_x = x_3 + x_10
x_label = ["三月{}日".format(i) for i in range(1, 32)]
x_label += ["十月{}日".format(i) for i in range(1, 32)]
plt.xticks(_x[::3], x_label[::3], rotation=45)
plt.yticks(fontsize=20)

# xy轴描述
plt.xlabel("日期", fontsize=15)
plt.ylabel("温度", fontsize=15)

plt.legend(loc="upper left")
plt.savefig("D:\\matplotlib可视化图\散点图.png")

plt.show()
