def print_file_info(file_name):
	try:
		f = open(file_name, 'r', encoding='UTF-8')
		content = f.read()
		print('文件全部内容如下:')
		print(content)
	except Exception as f:
		print(f"不存在这个文件{f}")
	else:
		f.close()


def append_to_file(file_name, data):
	with open(file_name, 'a', encoding='UTF-8') as a:
		a.write(data)


if __name__ == '__main__':
	print_file_info('test')
