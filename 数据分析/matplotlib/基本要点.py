from matplotlib import pyplot as plt

# 可以理解为画布
plt.figure(figsize=(20, 8), dpi=100)

x = range(2, 26, 2)

y = [15, 13, 12, 21, 43, 32, 43, 23, 23, 43, 43, 12]
# 画折线图的方法
plt.plot(x, y)
# 设置x轴刻度
# _x_lab = [i / 2 for i in range(4, 49)]
# plt.xticks(_x_lab[::3])
# plt.yticks(range(min(y), max(y)))
plt.savefig("C:\\Users\\何潇磊\\Pictures\\美女图.png")
plt.show()
