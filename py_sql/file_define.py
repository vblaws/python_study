# 有两套文件，一个是标准txt，另一个是json形式的,所以到定义一个抽象类，具体由子类实现
import json

from data_define import Record_data


class file_reader:
	
	def read_file(self) -> list[Record_data]:
		"""读取文件数据,读到的每一条对象转化为record对象,都封装为list返回"""
		pass


class Text_reader(file_reader):
	def __init__(self, path):
		self.path = path  # 记录文件的路径
	
	# 	实现抽象方法
	def read_file(self) -> list[Record_data]:
		f = open(self.path, 'r', encoding='utf-8')
		# 存储每一个record对象
		record_list: list[Record_data] = []
		for line in f.readlines():
			line = line.strip()  # 消除每一行读取到的回车符号
			data_list = line.split(',')
			# data_list[2]是数字，因为之后要参加计算，所以要转化为int类型
			record = Record_data(data_list[0], data_list[1], int(data_list[2]), data_list[3])
			record_list.append(record)
		f.close()
		return record_list


class Json_reader(file_reader):
	def __init__(self, path):
		self.path = path
	
	def read_file(self) -> list[Record_data]:
		record_list: list[Record_data] = []
		f = open(self.path, 'r', encoding='utf-8')
		
		for line in f.readlines():
			python_dict = json.loads(line)
			
			record = Record_data(python_dict['date'], python_dict['order_id'], python_dict['money'],
			                     python_dict['province'])
			print(record)
			record_list.append(record)
		return record_list


if __name__ == '__main__':
	text_reade = Text_reader('D:/2011年1月销售数据.txt')
	json_reade = Json_reader('D:/2011年2月销售数据JSON.txt')
# list1=text_reade.read_file()
# for i in list1:
# 	print(i)
# list2=json_reade.read_file()
# for i in list2:
# 	print(i)
