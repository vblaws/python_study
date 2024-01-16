from pymysql import Connection

from data_define import Record_data
from file_define import Text_reader, Json_reader

text_file_reader = Text_reader('D:/2011年1月销售数据.txt')
json_file_reader = Json_reader('D:/2011年2月销售数据JSON.txt')

jan_data: list[Record_data] = text_file_reader.read_file()
feb_data: list[Record_data] = json_file_reader.read_file()
# 将两个列表合并为一个列表
data_all: list[Record_data] = jan_data + feb_data
# 创建数据库连接
conn = Connection(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	autocommit=True  # 自动提交
)
# 选择数据库
conn.select_db('py_sql')
# 生成游标对象
cursor = conn.cursor()
for record in data_all:
	sql = (f"insert into orders(order_data,order_id,money,province) values ('{record.data}',"
	       f"'{record.order_id}'"
	       
	       f",{record.money},"
	       
	       f"'{record.province}')")
	# print(sql)
	cursor.execute(sql)

conn.close()
