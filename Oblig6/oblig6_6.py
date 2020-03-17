import datetime

""" This program is made as a solution to activity 1 of the 6th assignment 
	of IN1000 at UiO, fall 2019. """

def innlesing(fn="salgstall.txt"):
	""" Reads statistical data from a file,
	returns dictionary of values.
	Might as well have been donde with json.load(), and using
	json.dumps(), as this simplifies prettyprinting data.
	"""

	statistical_dict = dict()

	with open(fn, "r") as f:
		pairs = f.read().strip().split("\n")

	for key, value in [pair.split(" ") for pair in pairs]:
		if statistical_dict.get(key):  # returns None if non-existent
			statistical_dict[key] += int(value)
		else:
			statistical_dict[key] = int(value)
	return statistical_dict

def maanedensSalgsperson(data):
	return max(data, key=data.get)

def totaltAntallSalg(data):
	return sum(data.values())

def gjennomsnittSalg(data):
	return totaltAntallSalg(data)/len(data.keys())

def hovedprogram():
	my_data = innlesing()  # Activity 1.1

	monthly_employee = maanedensSalgsperson(my_data)  # Activity 1.2
	total_sales = totaltAntallSalg(my_data)  # Activity 1.3
	average_sales = gjennomsnittSalg(my_data)  # Activity 1.4

	# Activity 1.5
	print(f"Maanedens ansatte er Tina med {my_data[monthly_employee]} salg.")
	print()
	print(f"Aktive selgere denne maaneden: {len(my_data.keys())}")
	print(f"Total antall salg: {total_sales}")
	print(f"Gjennomsnittlig antall salg per salgsperson: {average_sales}")

if __name__ == '__main__':
	hovedprogram()  # Activity 1.6

""" This program is made as the solution to activity 2 of the 6th assignment of
	IN1000 at UiO, fall 2019. """

class Motorsykkel:
	# Activity 2.1
	def __init__(self, brand, reg_number, start_x=0):
		self.brand = brand
		self.reg_number = reg_number
		self.x = start_x

	# Activity 2.2
	def kjor(self, km):
		self.x += km

	# Activity 2.3
	def hentKilometerstand(self):
		return self.x

	# Activity 2.4
	def skrivUt(self):
		print(self)

	def __str__(self):
		return 	"Registreringsnummer: " + str(self.reg_number) + "\n" +\
				"Merke: " + str(self.brand) + "\n" +\
				"Kilometer: " + str(self.x)

# Activity 2.5
from motorsykkel import Motorsykkel as MC

def hovedprosedyre():
	# Activity 2.6
	my_mc0 = MC(brand="Harley Davidson", reg_number="X123456Y", start_x=0)
	my_mc1 = MC(brand="Harley Davidfather", reg_number="X123457A", start_x=10)
	my_mc2 = MC(brand="Harley Davidholy-spirit", reg_number="X123458F", start_x=3000)

	for bike in [my_mc0, my_mc1, my_mc2]:
		bike.skrivUt()
		print()

	# Activity 2.7
	my_mc2.kjor(50)
	print(my_mc2.hentKilometerstand())

if __name__ == '__main__':
	hovedprosedyre()  # Activity 2.8

""" This program is made as the solution to activity 4 of the
6th assignment of IN1000 at UiO, fall 2019. """
class Hund:
	def __init__(self, alder, vekt):  # Activity 4.1
		self.alder = alder
		self.vekt = vekt
		self.metthet = 10

	# Activity 4.2
	def get_alder(self):
		return self.alder

	def get_vekt(self):
		return self.vekt

	# Activity 4.3
	def spring(self):
		self.metthet -= 1
		if self.metthet < 5:
			self.vekt -= 1

	# Activity 4.4
	def spis(self, quantity):
		self.metthet += quantity
		if self.metthet > 7:
			self.vekt += 1

""" Test Hund.py """
def hovedprogram():
	my_dog = Hund(alder=10, vekt=5)
	print(my_dog.get_vekt(), my_dog.get_alder())

	my_dog.spis(3)
	print(my_dog.get_vekt(), my_dog.get_alder())
	my_dog.spring()
	print(my_dog.get_vekt(), my_dog.get_alder())
	my_dog.spis(3)
	print(my_dog.get_vekt(), my_dog.get_alder())


	for _ in range(12):
		my_dog.spring()
	print(my_dog.get_vekt(), my_dog.get_alder())


if __name__ == '__main__':
	hovedprogram()  # Activity 4.5

""" This program is made as the solution to activity 6 of the 6th assignment of
IN1000 at UiO, fall 2019. The idea is to have the definition of a person,
and construct a family tree of ancestors out of the known data. """

class Color:
	colours = {
		"lred": "\033[91m",
		"lgreen": "\033[92m",
		"yellow": "\033[93m",
		"default": "\x1b[0m"
	}
	@staticmethod
	def str(colour, str_):
		return Color.colours[colour] + str(str_) + Color.colours["default"]

class Person:
	def __init__(self, name, birthday=None, age=None,
	parents=list(), parent1=None, parent2=None, dead=False):

		self.name = name

		today = datetime.datetime.today()
		if birthday:
			self.birthday = datetime.datetime.strptime(birthday, "%d%m%Y")
			self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
		elif age:
			self.birthday = datetime.datetime.strftime("%d%m%Y", "0101"+str(datetime.datetime.today().year - self.age))
			self.age = age
		else:
			self.birthday = None
			self.age = None

		self.dead = dead
		if dead:
			self.age = -1

		self.parents = list(parents)
		if parent1:
			self.parents.append(parent1)
		if parent2:
			self.parents.append(parent2)

	def __str__(self):
		ancestors = ""
		if self.parents:
			ancestors = ancestors + "(" + u"\u2014".join(map(str, self.parents)) + ")"

		if self.dead:
			return ancestors + self.name +  Color.str("lred", u"\u271d")
		elif self.age:
			return ancestors + self.name +  Color.str("lgreen", self.age)
		else:
			return ancestors + self.name +  Color.str("yellow", "?")

ddgrandpa = Person("Rolf Arne", dead=True)
dgrandpa = Person(name="Rolf Arne a", parents=[ddgrandpa], dead=True)
dgrandma = Person(name="Vigdis")
dad = Person(name="Vidar", birthday="07051967", parents=[dgrandpa,dgrandma])

mgrandpa = Person(name="Leif Arvid", birthday="01011997", dead=True)
mgrandma = Person(name="Signe")
mom = Person(name="Tove Iren", birthday="01011961", parents=[mgrandma, mgrandpa], dead=True)

me = Person(name="Rolf Vidar", birthday="11031997", parent1=dad, parent2=mom)
print(dad, mom, me)
