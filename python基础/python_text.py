# name='lucy' if 2>1 else 'Chiek'
#
# print(name)

# 求出所有的素数
result=''

for i in range(2,101):
	flag=True
	for j in range(2,i-1):
		if i % j ==0:
			flag=False
			break
	if flag==True:
		result+=str(i)+','


print(result)
# 九九乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print(f"{i}*{j}={i*j} ",end="")

	print()

# 列表去重

my_list=[12,3,4,125,325,124,12,32,3,4,325]
result=[]
for item in my_list:
	if item not in result:
		# 如果添加过，则不会添加了
		result.append(item)

print(result)
# 统计字符出现的个数
# 格式:字符串.count(字符)
s='What are you doing'
print(f"字符o出现的个数为{s.count('o')}")
# 获取字符串下表
# 如果字符串重复，则会获取第一个出现字符下标
print(f"字符o的下标为{s.index('o')}")

# 分隔字符串变成一个新列表
my_str_list=s.split(' ')
print(my_str_list)
# 大小写转换
"""
lower():全部转换为小写
upper():全部转换为大写
swapcase():大写转换为小写,小写转化为大写
capitalize():将第一个字符设置为大写，其余为小写
title():将每个单词首字母大写，其余小写
"""

print(f"全部小写{s.lower()}")
print(f"全部大写{s.upper()}")
print(f"大写转化为小写，小写转化为大写{s.swapcase()}")
print(f"第一个字符设置为大写，其余小写{s.capitalize()}")
print(f"每个单词首字母大写{s.title()}")
my_dict={'Jack':15,'Mary':19,'Rose':11}
print(my_dict)
# 获取某个键的值
print(my_dict['Jack'])
# 修改某个键的值
my_dict['Mary']=10
print(my_dict['Mary'])
# 增加键值对
my_dict['Peter']=20
print(my_dict)
# 删除键值对
del my_dict['Rose']
print(my_dict)

# 复制字典
my_new_dict=my_dict.copy()
print(f"复制后的字典为{my_new_dict}")