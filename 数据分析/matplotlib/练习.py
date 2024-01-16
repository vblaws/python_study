import random

from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
from matplotlib import pyplot as plt
# 设置画布大小及dpi
plt.figure(figsize=(25, 8), dpi=120)

x = [i for i in range(120)]  # 时间
y = [random.randint(20, 35) for i in range(120)]  # 温度

plt.plot(x, y)

# xy轴添加文字描述
_xtick_lable = ["10点{}分".format(i) for i in range(60)]
_xtick_lable += ["11点{}分".format(i) for i in range(60)]
# rotation属性用来设置字体旋转角度
plt.xticks(x[::5], _xtick_lable[::5], rotation=45)
# 添加描述
plt.xlabel("时间")
plt.ylabel("温度，单位(:c)")
plt.title("10-12点每分钟温度变化情况")
plt.savefig("D:\\matplotlib可视化图\\练习.png")

plt.show()
