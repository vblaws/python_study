def test_func(func):
	result=func(2,5)
	print(result)
def coumper(x,y):
	return x*y
test_func(coumper)

test_func(lambda x,y:x+y)





