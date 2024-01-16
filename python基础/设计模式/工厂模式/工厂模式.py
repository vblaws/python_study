class Person:
	pass


class Worker:
	pass


class Nurse:
	pass


class Student:
	pass


# 工厂模式
class Factory:
	def get_person(self, person_type):
		if person_type == "w":
			return Worker()
		elif person_type == "n":
			return Nurse()
		else:
			return Student()


factory = Factory()
worker = factory.get_person("w")
nurse = factory.get_person("n")
student = factory.get_person("df")
