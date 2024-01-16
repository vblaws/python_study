import time

# text=f.read(2)
# print(text)

# new_text=f.readlines()
# print(new_text)

# content=f.readline()
# print(f"第一行内容为{content}")
# content=f.readline()
# print(f"第二行内容为{content}")
# for line in f:
# 	print(line)
#
# # 关闭文件
# f.close()

with open('file_text', 'r', encoding='UTF-8') as f:
	for line in f:
		print(f"每一行数据为{line}")
# 执行完以后，会自动把文件给关闭

time.sleep()