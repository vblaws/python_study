my_set={'黑马','黑马','你好','itheima'}
my_set_empty=set()
print(f"my_set内容是{my_set},类型为{type(my_set)}")
my_set.add('你在干什么')
print(my_set)
my_set.remove('你好')
print(my_set)
# 随机取出一个元素
element=my_set.pop()
print(element)
print(my_set)
my_set.clear()
print(my_set)
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"取出差集的结果是{set3}")
# 消除在集合1内和集合2相同的元素
set1.difference_update(set2)
print(set1)
set4=set1.union(set2)
print(f"合并后的结果为{set4}")
print(f"集合{set4}长度为{len(set4)}")
# 遍历集合
for i in set4:
	print(i)