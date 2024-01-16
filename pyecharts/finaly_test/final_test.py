from pyecharts.charts import *
from pyecharts.globals import *
from pyecharts.options import *

# my_list=[['a',10],['b',30],['c',90]]
#
# # # 匿名形式
# # my_list.sort(key=lambda element:element[1],reverse=True)
# # print(my_list)
# # 带参形式
# def my_choose_list(element):
# 	return element[1]
# my_list.sort(key=my_choose_list,reverse=True)
# print(my_list)

# 打开文件
f = open('D:/1960-2019全球GDP数据.csv', 'r', encoding='GB2312')

# 读取数据,存储为列表
dataLines = f.readlines()
f.close()
# 删除第一行
dataLines.pop(0)
# 定义一个字典对象保存数据
data_dict = {}
# 拿到每一行数据
for line in dataLines:
	year = int(line.split(',')[0])  # 年份
	country = line.split(',')[1]  # 国家
	GDP = float(line.split(',')[2])  # GDP
	# 判断字典里面有没有指定的key
	try:
		data_dict[year].append([country, GDP])
	except KeyError as e:
		data_dict[year] = []
		data_dict[year].append([country, GDP])
# print(data_dict)
# 按照年份排序,存储为列表
sorted_year_list = sorted(data_dict.keys())
# 创建时间线对象
timeline = Timeline(
	{'theme': ThemeType.LIGHT}
)
for year in sorted_year_list:
	data_dict[year].sort(key=lambda element: element[1], reverse=True)
	# 得到本年份前8名的国家
	year_data = data_dict[year][0:8]
	# 创建列表
	x_data = []
	y_data = []
	for country_gdp in year_data:
		x_data.append(country_gdp[0])  # X轴添加数据
		y_data.append(country_gdp[1] / 100000000)  # Y轴添加gdp数据
	
	# 构架柱状图
	bar = Bar()
	# 反转数据，让大的在上面
	x_data.reverse()
	y_data.reverse()
	bar.add_xaxis(x_data)
	bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position='right'))
	# 反转X轴和Y轴
	bar.reversal_axis()
	# 设置每一年图表标题
	bar.set_global_opts(
		title_opts=TitleOpts(title=f"{year}年GDP前八的国家")
	)
	# 设置时间线标题
	timeline.add(bar, f"{year}")
# 设置自动播放
timeline.add_schema(
	play_interval=1000,
	is_timeline_show=True,
	is_auto_play=True,
	is_loop_play=False,
)
# 网页名子
timeline.render("全球GDP前8的国家.html")
