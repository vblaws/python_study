from module import *
# module.test(10,20)
testA(10,20)
try:
	testB(10,20)
except Exception as a:
	print("出现错误")
	print(a)