class Animal:
	# 空实现 
	def speak(self):
		pass

class Dog(Animal):
	def speak(self):
		print("汪汪叫")


class Cat(Animal):
	def speak(self):
		print("喵喵叫")
# 		类型注解为Animal类
def make_noise(animal:Animal):
	animal.speak()

dog=Dog()
cat=Cat()

make_noise(dog)
make_noise(cat)