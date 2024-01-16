# 方法1
# count=0
# with open('word.txt','r',encoding='UTF-8') as f:
# 	for line in f:
# 		if 'itheima' in line:
# 			count+=1
#
# 方法2  一行一行读取
# f=open('word.txt','r',encoding='UTF-8')
#
# count=0
#
# for line in f:
# 	content=line.strip()# 去除字符串前后的空格和换行符
# 	words=content.split(' ')# 以空格作为分隔符
# 	for word in words:
# 		# print(word)
# 		if word == 'itheima':
# 			count+=1
# f.close()
# print(f"itheima出现的次数为{count}")
# 方法3 一次性读取

f=open('word.txt', 'r', encoding='UTF-8')
content=f.read()
count=content.count('itheima')
print(f"itheima出现的次数{count}")
f.close()
