class AC:
	def cool_wind(self):
		"""制冷"""
		pass
	def hot_wind(self):
		"""制热"""
		pass
	def swing_l_r(self):
		"""左右摆风"""
		pass


class Ge_li(AC):
	def cool_wind(self):
		"""制冷"""
		print("格力核心制冷")

	def hot_wind(self):
		"""制热"""
		print("格力核心制热")
	def swing_l_r(self):
		"""左右摆风"""
		print("格力核心左右摆风")

class Mei_di(AC):
	def cool_wind(self):
		"""制冷"""
		print("美的核心制冷")

	def hot_wind(self):
		"""制热"""
		print("美的核心制热")

	def swing_l_r(self):
		"""左右摆风"""
		print("美的核心左右摆风")
# 传入一个对象
def make_cool(ac:AC):
	ac.cool_wind()
geli=Ge_li()
meidi=Mei_di()

make_cool(geli)
make_cool(meidi)
