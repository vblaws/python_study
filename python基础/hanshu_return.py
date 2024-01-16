def test_return():
	return 1,2,'Hello World'
# 性别默认为男，如果传入参数是修改了，则用修改后的值
def user_info(name,age,gander='男'):
	print(f"你的名字{name},你的年龄{age}，你的性别{gander}")
x,y,str=test_return()
print(x)
print(y)
print(str)


# user_info(name='hxl',12,gander='男') 此为错误的，因为位置参数没有放在关键字参数前面
# 关键字参数可以顺序打乱

user_info('hxl',age=12)
user_info('hxl',age=12,gander='女')

# 位置传递,为了规范最好写args,
# 会将传入的参数转化为元组
def user_info_where(*args):
	print(args)

user_info_where('TOm',12,12,'你好','你不好')
# 关键字传递,为了规范最好写kwargs,所有键值对会被自动转换成字典
def user_info_dict(**kwargs):
	print(kwargs)

user_info_dict(name='hxl',age=11,address='suzhou')

def user_info_new_yuanzu(*args):
	return args

def user_info_yuanzu(user_info_new_yuanzu):
	tuple=user_info_new_yuanzu('tom','kitty',12)
	print(f"元内容为{tuple}")

user_info_yuanzu(user_info_new_yuanzu)