class Phone:
	IMEI=None
	produce='itheima'

	def call_by_5g(self):
		print("使用5g进行通话")
	
class My_phone(Phone):

	produce ='itcast'

	def call_by_5g(self):
		print("开启CPU单核模式，确保省电")
		# 调用父类成员方法,方式1
		print(f"父类的厂商是{Phone.produce}")
		Phone.call_by_5g(self)
		# 方法2
		print(f"父类的厂商{super().produce}")
		super().call_by_5g()
		print("关闭单核模式，确保性能")



my_phone=My_phone()

my_phone.call_by_5g()
print(f"{my_phone.produce}")