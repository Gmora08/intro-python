from person import Person


class Sensei(Person):
	
	def __str__(self):
		return self.get_full_name()
