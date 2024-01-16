
dict1={'ws':11,'gqr':20,'llw':12}
dict2={'ws':20,'hxl':17}
# 如果dict2中包含有dict1内的键值对，则会被覆盖dict1内的value

# 如果dict2中包含dict1内不存在的，则会添加
dict1.update(dict2)
print(dict1)
# 获取所有的键值,items(),会返回一个二维的可迭代对象，类似于二维的元组列表
my_list=dict1.items()
print(f"获取说有的键值对{my_list}")
print(f"获取所有的键{dict1.keys()}")
print(f"获取所有的值{dict1.values()}")
# 遍历
for key,value in my_list:
	result=f'key:{key},value:{value}'
	print(result)