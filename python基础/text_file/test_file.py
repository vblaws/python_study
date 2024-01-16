other=open('bill.txt.bak', 'a', encoding='UTF-8')
with open('test', 'r', encoding='UTF-8') as f:
	for line in f:
		if '测试' in line:
			continue
		else:
			other.write(line)


other.close()

