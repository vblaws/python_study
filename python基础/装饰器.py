# 装饰器：在不破坏目标函数原有的代码和功能的前提下，为目标函数添加功能
# def outer(func):
# 	def inner():
# 		print("我要睡觉了")
# 		func()
# 		print("我要起床了")
#
# 	return inner
#
#
# def sleep():
# 	import time
# 	import random
# 	print("睡眠中")
# 	time.sleep(random.randint(1, 10))
#
#
# fn1 = outer(sleep)
# fn1()
def outer(func):
	def inner():
		print("我要睡觉了")
		func()
		print("我要起床了")
	
	return inner


@outer
def sleep():
	import time
	import random
	print("睡眠中")
	time.sleep(random.randint(1, 10))


sleep()
