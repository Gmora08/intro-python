from person import Person
from senseis.sensei import Sensei

class Student(Person):

	def __init__(self, *args, **kwargs):
		self.belt = kwargs.pop('belt', None)
		self.senseis = []

		super(Student, self).__init__(*args, **kwargs)

	def add_sensei(self, sensei):
		self.senseis.append(sensei)

	def print_senseis(self):
		for sensei in self.senseis:
			print sensei

if __name__ == '__main__':
	gus = Student('Gustavo', 23, 'Mora', belt='White')
	
	diego = Sensei('Diego', 'De Granda', 27)
	sergio = Sensei('Sergio', 'Malvaez', 23)
	pablo = Sensei('Pablo', 'Trinidad', 18)

	gus.add_sensei(diego)
	gus.add_sensei(sergio)
	gus.add_sensei(pablo)

	gus.print_senseis()

