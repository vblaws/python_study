# # 异常捕获方法
# try:
# 	f=open('Hello.txt','r',encoding='UTF-8')
# except:
# 	print("文件不存在只读模式下出现错误，现在使用写入模式创建")
# 	f=open('Hello.txt','w',encoding='UTF-8')
#
# # 捕获指定的异常
# try:
# 	print(name)
# except NameError as e:# e记录异常具体信息
# 	print("变量未定义错误")
# 	print(e)
# 捕获多个异常
try:
	print("name")

except(NameError,ZeroDivisionError) as e:
	print("变量未定义错误或除0错误")
	print(e)
else:
	print("没有出现异常")
finally:
	print("结束")