# 设置显示中文字体
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]

x = [i for i in range(11, 31)]
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1]

plt.figure(figsize=(15, 10), dpi=80)
# 画图
plt.plot(x, y_1,
         label="自己",
         color='r',
         linestyle='-',
         linewidth=10,
         alpha=0.5
         )
plt.plot(x, y_2,
         label="同桌",
         color='g',
         linestyle=":",
         linewidth=10,
         alpha=0.5
         )

x_label = ["{}岁".format(i) for i in range(11, 31)]
plt.xticks(x, x_label, rotation=45, fontsize=20)
plt.yticks(fontsize=20)

# 描述
plt.xlabel("岁数", fontsize=25)
plt.ylabel("交到女友数量", fontsize=25)

plt.title("恋爱经历", fontsize=25)
plt.savefig("D:\\matplotlib可视化图\\两人女友图.png")
# 绘制网格
plt.grid(alpha=0.4)
# 显示图例
plt.legend(loc="upper left")

plt.show()
