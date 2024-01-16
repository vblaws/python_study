# # 简单的闭包写法
# def outer(logo):
# 	def inner(msg):
# 		print(f"<{logo}><{msg}><{logo}>")
#
# 	return inner
#
#
# fn1 = outer("你好")  # 此时类型为函数function
# print(type(fn1))
# fn1("我是何潇磊")
# fn1("我是刘立文")
def outer(num1):  # 想要修改外部变量的值可以使用nonlocal关键字，设外部变量为我的金额,内部函数为我的存钱数额
	# 这样我的金额就不能被随意修改
	def inner(num2):
		nonlocal num1
		num1 += num2
		print(num1)
	
	return inner


fn1 = outer(1000)
fn1(20)
fn1(30)


# 练习代码

def accout_moneu(money=0):
	def cqqq(num, cun_or_qu=True):
		nonlocal money  # 用nonlocal可以让内部函数访问外部函数值
		if cun_or_qu:
			money += num
			print(f"存钱+{num},现在钱数为{money}")
		else:
			money -= num
			print(f"取钱-{num},现在钱数为{money}")
	
	return cqqq


fn1 = accout_moneu()
fn1(10)
fn1(20, False)  # 这边false可以空着，为缺省参数,默认为True
