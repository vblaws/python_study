class Phone:
		# 当前手机默认电压，一个私有成员变量
		__current_voltage=0.5
		# 手机单核运行状态，一个私有成员方法
		def __keep_single_core(self):
			print("手机正在已单核模式运行,更加省点")
		def call_by_5G(self):
			if self.__current_voltage>1:
				print("5g模式已开启")
			else:
				self.__keep_single_core()
				print("电量不足，无法使用5g通话")


phone=Phone()

phone.call_by_5G()