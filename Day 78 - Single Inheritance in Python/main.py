class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat

class animal:
	def __init__(self,name,sound,color):
		self.name=name
		self.sound=sound
		self.color=color
	def music(self):
		print(f"the sound of my {self.name} is {self.sound}")
class cat(animal):
	def showdetails(self):
			print(f"the color of my {self.name} is {self.color}")
	def rang(self):
		print(f"the voice of my {self.name} is {self.sound}")

c=cat("cat","meow","white")
c.showdetails()
c.rang()
a=animal("dog","bark","black")
a.music()