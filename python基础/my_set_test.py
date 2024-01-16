# 定义一个空集合
my_set=set()

my_list=['黑马程序猿','传智播客','黑马程序员','传智播客','itheima','tcast','itheima','itcast','best']
# 遍历列表
for i in my_list:
	print(i)
print('列表元素添加到集合')
for j in my_list:
	my_set.add(j)


print(f"集合添加后的元素为{my_set}")
