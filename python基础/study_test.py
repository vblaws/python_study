my_str='万过薪月，员序程马黑来，nohtyP学'
result=my_str[9:4:-1]
print(result)
# 先倒序，然后取出
result1=my_str[::-1][9:14]
print(result1)
# 先取出，再倒序
result2=my_str[5:10][::-1]
print(result2)
# split分隔“，”，replace替换“来”为空,倒序字符串
result3=my_str.split("，")[1].replace("来","")[::-1]
print(result3)