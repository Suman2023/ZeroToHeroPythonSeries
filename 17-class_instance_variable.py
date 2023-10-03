# Class Variable vs Instance/Object Variable

class Circle:
	# Class variables are defined outside functions/methods
	PI = 3.14  # class Variable #immutable

	list1 = [] #Mutable

	def __init__(self,radius):
		# Instance Variable are defined inside methods
		self.radius = radius # Instance Variable
		self.list2 = []

	def get_area(self):
		# Instance variable can be defined isnisde any methods
		# self.name = "lets Code Togetehr"
		return self.PI * pow(self.radius, 2)

	@classmethod
	def change_pi(cls):
		# print(cls)
		cls.PI = 0


# Instance variable are part of that particular instance
# Class variable are part of all instance

circle1 = Circle(10)


circle2 = Circle(12)

# ACessing variable
print(circle1.radius)
print(circle2.radius)

print(circle1.PI)
print(circle2.PI)

print(f"Area of Circle 1: {circle1.get_area()}")
print(f"Area of Circle 2: {circle2.get_area()}")


# Acesing class variable

print(Circle.PI)

print(f"Area of Circle 1: {circle1.get_area()}")
circle1.radius = 0
print(f"Area of Circle 1: {circle1.get_area()}")
print(f"Area of Circle 2: {circle2.get_area()}")
print(f"Area of Circle 1: {circle1.get_area()}")
print(f"Area of Circle 2: {circle2.get_area()}")

Circle.PI = 0 # Not a proper way to do (not recommended)
circle1.get_area()
Circle.change_pi() #(recommended way)

print(f"Area of Circle 1: {circle1.get_area()}")
print(f"Area of Circle 2: {circle2.get_area()}")



#Mutability Factor

# Immutable class variable
circle1 = Circle(10)

circle2 = Circle(12)

circle1.PI = 1

print(circle1.get_area())
print(circle2.get_area())


# Mutable class variable
circle1 = Circle(10)

circle2 = Circle(12)

circle1.list1.append(100) # For class variable

# print(circle1.get_area())
# print(circle2.get_area())

print(circle1.list1)
print(circle2.list1)

circle1.list2.append(100) # Instance Variable

print(circle1.list2)
print(circle2.list2)


# Use Mutable Type only for class variable if you dont want it to be updated for all instance.
# try using mutable type as instance variable
