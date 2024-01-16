import os


def get_files_recwsion_from_dir(path):
	"""
	从指定文件夹使用递归，获取所有的文件列表
	:param path:
	:return list:包含全部的文件，如果目录不存在，则返回一个空list
	"""
	file_list = []
	if os.path.exists(path):
		for f in os.listdir(path):
			new_path = path + "/" + f
		if os.path.isdir(new_path):
			file_list += get_files_recwsion_from_dir(new_path)
		else:
			file_list.append(new_path)
	else:
		print(f"指定的目录{path}不存在")
		return []
if __name__ == '__main__':
    get_files_recwsion_from_dir()