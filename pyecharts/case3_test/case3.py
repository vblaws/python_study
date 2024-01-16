import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open('D:/疫情.txt', 'r', encoding='UTF-8')
map_data = f.read()
# json转化为python字典
map_data_python = json.loads(map_data)

# 定义一个绘图时需要的列表
data_list = []
trend_data_list = map_data_python['areaTree'][0]['children']
for province_data in trend_data_list:
	province_name = province_data['name']  # 省份名称
	province_chile = province_data['total']['confirm']  # 确诊人数
	# 处理省份不匹配问题
	if province_name == "新疆":
		province_name = "新疆维吾尔自治区"
	elif province_name == "广西":
		province_name = "广西壮族自治区"
	elif province_name == "宁夏":
		province_name = "宁夏回族自治区"
	elif province_name in ["内蒙古", "西藏"]:
		province_name = province_name + "自治区"
	elif province_name in ["北京", "天津", "重庆", "上海"]:
		province_name = province_name + "市"
	elif province_name in ["香港", "澳门"]:
		province_name = province_name + "特别行政区"
	else:
		province_name = province_name + "省"
	
	# 组装成一个元祖
	data_list.append((province_name, province_chile))

# 创建一个地图对象
map = Map()
map.set_global_opts(
	toolbox_opts=ToolboxOpts(is_show=True),
	title_opts=TitleOpts(title='全国疫情地图'),
	# 视觉映射配置项
	visualmap_opts=VisualMapOpts(
		is_show=True,  # 是否显示
		is_piecewise=True,  # 是否分段
		# 具体分段
		pieces=[
			{'min': 1, 'max': 99, 'label': '1-99人', 'color': '#CCFFFF'},
			{'min': 10, 'max': 999, 'label': '100-999人', 'color': '#00FFFF'},
			{'min': 1000, 'max': 4999, 'label': '1000-4999人', 'color': '#a0222f'},
			{'min': 5000, 'max': 9999, 'label': '5000-99999人', 'color': '#4B0082'},
			{'min': 10000, 'max': 99999, 'label': '10000-999999人', 'color': '#2086bc'},
			{'min': 100000, 'label': '100000万以上', 'color': '#a0222f'},
		]
	)
)
# 添加数据

map.add('各省份确诊人数', data_list, 'china')
# 生成图表
map.render()
# 关闭文件

f.close()
