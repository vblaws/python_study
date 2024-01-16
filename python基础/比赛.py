import csv

from pymysql import Connection

conn = Connection(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	autocommit=True  #设置自动提交
)

cursor = conn.cursor()
conn.select_db("bisai")
with open('D:\\output.csv', 'r', encoding='utf-8') as file:
	reader = csv.reader(file)
	for f in list(reader)[1:]:# 从第一行开始读取
		sql = 'INSERT INTO t_comment(title_name, city, name, date)  VALUES (%s,%s,%s,%s)'
		cursor.execute(sql,(f[0],f[1],f[2],f[3]))
cursor.close()
conn.close()
