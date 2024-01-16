class Phone:
	def __init__(self, name, year, beauty):
		self.name = name
		self.year = year
		self.beauty = beauty
	
	# 大于和小于
	def __lt__(self, other):
		return self.year < other.year
	
	# 大于等于
	def __le__(self, other):
		return self.year <= other.year
	
	# 等于
	def __eq__(self, other):
		return self.year == other.year
	
	def ring(self):
		import winsound
		winsound.Beep(2000, 3000)


xiaomi = Phone('小米14', 1, '好看')
print(f"手机名字叫{xiaomi.name},已经出了{xiaomi.year}年了,他非常的{xiaomi.beauty}")
# xiaomi.ring()
# print("手机响铃了")
iphone = Phone('iphone15', 4, '不错')

print(xiaomi < iphone)
print(xiaomi <= iphone)
# 如果没有eq魔术方法，则==默认比较内存地址
print(xiaomi == iphone)
