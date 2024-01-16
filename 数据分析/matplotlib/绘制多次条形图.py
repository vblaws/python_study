from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(40, 16), dpi=80)
x = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠:英雄归来", "战狼2"]
y_16 = [15746, 312, 4497, 319]
y_15 = [12357, 156, 2045, 168]
y_14 = [2358, 399, 2358, 362]

border_width = 0.2

# 要把x轴向右移动一点,否则会重合
x_14 = list(range(len(x)))
x_15 = [i + border_width for i in x_14]
x_16 = [i + border_width * 2 for i in x_14]

plt.bar(x_14, y_14, width=border_width, label='九月14号', color='orange')
plt.bar(x_15, y_15, width=border_width, label='九月15号')
plt.bar(x_16, y_16, width=border_width, label='九月16号')

plt.legend(loc='upper left')
plt.xticks(x_15, x)  # 将中间的电影名字改掉就可以了
plt.savefig("D:\\matplotlib可视化图\多次条形图.png")

plt.show()
