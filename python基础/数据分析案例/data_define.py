class Record_data:
	def __init__(self,data,order_id,money,province):
		self.data=data
		self.order_id=order_id
		self.money=money
		self.province=province
	# 能够使打印对象的时候，打印这串字符串
	def __str__(self):
		return f'{self.data},{self.order_id},{self.money},{self.province}'




