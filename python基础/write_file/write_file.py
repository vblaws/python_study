f=open('python.txt', 'w', encoding='UTF-8')
f.write('Hello World')# 将内容写入到内存中
# f.flush()# 讲内容写入到文件中
f.close()# close方法内置flush方法