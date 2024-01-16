import random
from typing import Union

var_1: int = 10
var_2: str = 'itheima'
var_3: bool = True


class Student:
	pass


str: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {'heima': 12}

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, bool, float] = (1, True, 1.1)
my_dict: dict[str, int] = {'heima': 12}
# 取一个1到10的随机数
var_4 = random.randint(1, 10)  # type:int


def add(x: int, y: int):
	return x + y


print(f"5和1相加为{add(5, 1)}")
my_list: list[Union[int, str]] = [12, 214, 12, '124', '124']
my_dict: dict[str, Union[str, int]] = {'nihao': 1, 'nihao': '你好'}
