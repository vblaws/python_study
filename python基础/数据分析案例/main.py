from pyecharts.options import *
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from file_define import Text_reader,Json_reader,file_reader
from data_define import Record_data


text_file_reader=Text_reader('D:/2011年1月销售数据.txt')
json_file_reader=Json_reader('D:/2011年2月销售数据JSON.txt')

jan_data:list[Record_data]=text_file_reader.read_file()
feb_data:list[Record_data]=json_file_reader.read_file()
# 将两个列表合并为一个列表
data_all:list[Record_data]=jan_data+feb_data
# 开始数据计算
data_dict={}
# 理解
for record in data_all:
	if record.data in data_dict.keys():

		data_dict[record.data]+=record.money
	else:
		data_dict[record.data]=record.money

bar=Bar(
	init_opts=InitOpts(ThemeType.LIGHT)
)

bar.add_xaxis(list(data_dict.keys()))# python3以后字典.keys()方法返回的是一个可迭代序列，而不是列表
bar.add_yaxis('销售额',list(data_dict.values()),label_opts=LabelOpts(is_show=False)) # 添加y周数据
bar.set_global_opts(
	title_opts=TitleOpts(title='每日销售额')

)

bar.render('每日销售额柱状图.html')