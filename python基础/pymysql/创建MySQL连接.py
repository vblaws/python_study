from pymysql import Connection
# 获取到数据库连接对象
conn = Connection(
	host='127.0.0.1',
	port=3306,
	user='root',
	password='123456',
	# 自动确认数据更改
	autocommit=True
)
# 生成游标对象
cursor = conn.cursor()
# 用数据库连接对象选择一个数据库
conn.select_db('local_db')
# 用游标对象进行sql语句，不带查询属性的
# cursor.execute('CREATE TABLE Student(id int,name varchar(255),age int)')
# 数据更改 ,通过代码确认更改,现已自动确认
# cursor.execute('insert into users values(1,"ws",12)')
# cursor.execute('insert into users values(2,"hxl",15)')
# 数据库连接对象.commit()确认
# conn.commit()
# 查询语句,带查询属性的
cursor.execute('SELECT * FROM users')
# 获取返回结果，是一个元祖里面嵌套元祖，一行则为一个元祖元素
result:tuple=cursor.fetchall()
print(result)
for r in result:
	print(r)
# print(conn.get_server_info())
conn.close()