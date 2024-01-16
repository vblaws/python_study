# 对list切片
my_list=[1,2,3,4,5,6]
# 步长为1通常不写
result=my_list[1:4]
print(result)
# 对tuple切片
my_tupel=(0,1,2,3,4,5,6)
# 从头截到位，步长为1省略
result2=my_tupel[:]
print(result2)
# 对str切片,从头开始，到最后一个结束，步长为2


my_str='nihaoa ni zai gan shen me'
# 步长为负，反向取
result3=my_str[::-1]
print(result3)
# 对列表切片从3开始，到1结束,步长为-1
my_list=[0,1,2,3,4,5,6]
result4=my_list[3:1:-1]
print(result4)
# 对元组切片，从头开始，到尾结束，步长为-2

my_tupel=(0,1,2,3,4,5,6)

result6=my_tupel[::-2]
print(result6)





