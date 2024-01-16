import threading
import time


def dance(doing):
	while True:
		print(f"我在{doing}，啦啦啦啦\n")
		time.sleep(1)


def sing(msg):
	while True:
		print(f"我在唱{msg},啦啦啦啦\n")
		time.sleep(1)


if __name__ == '__main__':
	# 创建一个唱歌的线程
	sing_thread = threading.Thread(target=sing, args=("稻香",))  # args元祖传参
	# 创建一个跳舞的线程
	dance_thread = threading.Thread(target=dance, kwargs={"doing": "极乐净土"})  # kwargs:字典传参
	# 让线程启动
	sing_thread.start()
	dance_thread.start()
