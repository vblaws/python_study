from pymysql import Connection
from pyspark import *


conn=Connection(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	autocommit=True
)
# 选择数据库
conn.select_db('py_sql')
cursor=conn.cursor()
cursor.execute("select * from orders")
result:tuple=cursor.fetchall()
# for i in result:
# 	print(f"{{'data':{i[0]},'order_id':{i[1]},'money':{i[2]},'province':{i[3]}}}")
f=open('数据文件.txt','w',encoding='utf-8')
for i in result:
	f.write(f"{{'data':{i[0]},'order_id':{i[1]},'money':{i[2]},'province':{i[3]}}}")
f.close()
