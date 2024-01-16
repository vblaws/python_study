__all__=['testA']# 只能使用testA
def testA(a, b):
	print(a+b)

def testB(a,b):
	print(a-b)
# 防止被另外一个类调用时执行测试函数内,只有在这个类中运行才能执行
# if __name__ == '__main__':
#     testA(10,20)
