from pyecharts.charts import Line
#
from pyecharts.options import *

# 实例化对象

line=Line()

# 全局配置项
line.set_global_opts(
	title_opts=TitleOpts(title="GDP简略图", pos_left="center",pos_bottom="1%"),
	legend_opts=LegendOpts(is_show=True),
	toolbox_opts=ToolboxOpts(is_show=True),
	visualmap_opts=VisualMapOpts(is_show=True),

)

line.add_xaxis(['美国','中国','日本'])
line.add_yaxis('GDP1',[10,100,40])
line.render()