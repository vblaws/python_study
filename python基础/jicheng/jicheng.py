# 单继承
class Phone:
	IMEI = None
	produce = 'HUAWEI'

	def call_by_4g(self):
		print("4g通话")


class new_phone(Phone):
	face_id = '11100'

	def call_by_5g(self):
		print("5g通话")


iphone15 = new_phone()
print(f"手机品牌为{iphone15.produce}")
iphone15.call_by_4g()
iphone15.call_by_5g()
print(f"FACE_ID:{iphone15.face_id}")
# 多继承
class NFC_read:
	nfc_type='第五代'
	produce='huawei'

	def read_card(self):
		print("NFC已启动，请读卡")
	def write_card(self):
		print("NFC写卡,请写入")
class RemtoeControl:
	re_type="红外遥控"

	def control(self):
		print("红外遥控启动")

class Xiao_mi(NFC_read,RemtoeControl,new_phone):
	pass

my_xiaomi14=Xiao_mi()

my_xiaomi14.call_by_4g()
my_xiaomi14.call_by_5g()
my_xiaomi14.control()
my_xiaomi14.write_card()
my_xiaomi14.read_card()
