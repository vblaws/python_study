import json
from pyecharts.charts import Line
# 导入配置包
from pyecharts.options import *

# 处理数据
f_us=open('D:/美国.txt','r',encoding='UTF-8')
us_data=f_us.read()

f_jp=open('D:/日本.txt','r',encoding='UTF-8')
jp_data=f_jp.read()

f_in=open('D:/印度.txt','r',encoding='UTF-8')
in_data=f_in.read()
# 去不合JSON规范的开头
us_data=us_data.replace('jsonp_1629344292311_69436(','')
jp_data=jp_data.replace('jsonp_1629350871167_29498(','')
in_data=in_data.replace('jsonp_1629350745930_63180(','')
# 去不合JSON规范的结尾
us_data=us_data[:-2]
jp_data=jp_data[:-2]
in_data=in_data[:-2]
# JSON转Python字典
us_data_python=json.loads(us_data)
jp_data_python=json.loads(jp_data)
in_data_python=json.loads(in_data)
# 获trend key
trend_data_us=us_data_python['data'][0]['trend']
trend_data_jp=jp_data_python['data'][0]['trend']
trend_data_in=in_data_python['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年(到315下标结束)
x_data_us=trend_data_us['updateDate'][:314]
x_data_jp=trend_data_jp['updateDate'][:314]
x_data_in=trend_data_in['updateDate'][:314]
# 获取确认数据，用于y轴，取2020年(到315下标结束)
y_data_us=trend_data_us['list'][0]['data'][:314]
y_data_jp=trend_data_jp['list'][0]['data'][:314]
y_data_in=trend_data_in['list'][0]['data'][:314]
# 生成图表
line=Line()
# 设置全局参数
line.set_global_opts(
	title_opts=TitleOpts(title="2020年美日印三国疫情情况图", pos_left="center",pos_bottom="1%"),
	legend_opts=LegendOpts(is_show=True),
	toolbox_opts=ToolboxOpts(is_show=True),
	visualmap_opts=VisualMapOpts(is_show=True),
)
line.add_xaxis(x_data_us) # X轴是公用的，只用一个国家就可以了
# Y轴不共用,要添加三份数据
line.add_yaxis('美国确诊人数',y_data_us,label_opts=LabelOpts(is_show=False))# 标签设置为不显示
line.add_yaxis('日本确诊人数',y_data_jp,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数',y_data_in,label_opts=LabelOpts(is_show=False))
# 生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
