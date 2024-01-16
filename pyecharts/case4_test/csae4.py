import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open('D:/疫情.txt', 'r', encoding='UTF-8')

data = f.read()

data_dict = json.loads(data)
# 存储数据
data_list = []
trend_dict = data_dict['areaTree'][0]['children'][3]['children']

for country_item in trend_dict:
	country_name = country_item['name'] + '市'
	country_confirm = country_item['total']['confirm']
	# 存储元祖
	data_list.append((country_name, country_confirm))
# 手动添加
data_list.append(('济源市', 10000))
# 创建地图对象
map = Map()

map.set_global_opts(
	title_opts=TitleOpts(title='河南省疫情地图'),
	visualmap_opts=VisualMapOpts(
		is_show=True,
		is_piecewise=True,
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
map.add('河南省疫情分布图', data_list, '河南')
# 构图
map.render()
# 关闭文件
f.close()
