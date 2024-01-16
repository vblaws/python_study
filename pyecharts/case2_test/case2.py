from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 构建一个地图对象
map = Map()
# 全局化配置
map.set_global_opts(
	visualmap_opts=VisualMapOpts(
		is_show=True,
		# 手动指定范围
		is_piecewise=True,
		# 具体范围制定
		pieces=[
			{'min': 1, 'max': 9, 'label': '1-9人', 'color': '#84cff5'},
			{'min': 10, 'max': 99, 'label': '10-99人', 'color': '#2086bc'},
			{'min': 100, 'max': 499, 'label': '10-499人', 'color': '#a0222f'},
		]
	)
)
# 数据,列表里的元祖
data = [
	('北京市', 2),
	('上海市', 19),
	('湖南省', 29),
	('台湾省', 39),
	('广东省', 499)
]
# 添加元素
map.add('测试地图', data, 'china')
# 生成地图
map.render()

