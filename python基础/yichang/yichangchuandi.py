def func1():
	print("func1开始")
	num=1/0
	print("func1结束")

def func2():
	print("func2开始")
	func1()
	print("func2结束")


try:
	func2()
except Exception as e:
	print(f"发现异常{e}")