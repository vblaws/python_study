from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *


bar1=Bar()

bar1.add_xaxis(['中国','美国','英国'])

bar1.add_yaxis('GDP',[30,20,10],label_opts=LabelOpts(position='right'))
# 反转xy轴
bar1.reversal_axis()

bar2=Bar()

bar2.add_xaxis(['中国','美国','英国'])

bar2.add_yaxis('GDP',[100,68,49],label_opts=LabelOpts(position='right'))
# 反转xy轴
bar2.reversal_axis()

bar3=Bar()

bar3.add_xaxis(['中国','美国','英国'])

bar3.add_yaxis('GDP',[301,201,101],label_opts=LabelOpts(position='right'))
# 反转xy轴
bar3.reversal_axis()
# 创建时间线对象
time_line=Timeline(
	# 改变主题，在创建时间线对象时，在里面添加一个字典，如下
	{'theme':ThemeType.LIGHT}
)
# 设置自动播放
time_line.add_schema(
	play_interval=1000,
	is_timeline_show=True,
	is_auto_play=True,
	is_loop_play=True
)
time_line.add(bar1,'2020GDP')
time_line.add(bar2,'2021GDP')
time_line.add(bar3,'2022GDP')
# 用时间线绘图，不是bar对象了
time_line.render()