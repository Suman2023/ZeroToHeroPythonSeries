# class

# So, a class is like a blueprint, a plan, or a recipe that defines how to create objects.

# class itself is not real object its just a blueprint to create one.
# The objects will have its characteristics(attributes) and actions
# (methods/functions)

# Blueprint for pottery:  that is the class 
# Real objects like: Pot, Vase, Plate


# blueprint
class Pottery:
	# class variables/ charcteristics
	heated = True

	# special function
	# called automatically
	# called constructor or initializer
	def __init__(self, material, color, type):
		# print("Called __init__")

		# This are the charcteristics of that particular object
		# objects variables
		self.material = material
		self.color = color
		self.type = type
		self.heated = Pottery.heated  # this is how class variable are accesed
		

	# self says that function/method that this is specific to that particular object this is called for
	def set_color(self, color):
		self.color = color


	def is_heated(self, heated):
		self.heated = heated

	# This is what you get when you print the object created
	# use this functiopn to make it user friendly
	def __str__(self):
		return f"Object of Pottery with characteristics: {self.material}, {self.color} {self.type}"


# if there is no __init__ or no arguments inside init other then self
# pot = Pottery()

# here pot is the real object
pot = Pottery("Clay", "Brown", "Traditional")

# Here plate is different object created using the same blueprint
plate = Pottery("Stoneware", "White", "Functional")
# print(pot)

# Accessing the characteristics
# name of teh object + dot + characteristics_name

# print(pot.material)


# print("Pot Before\n")
# # print("Pot")
# print(pot.material)
# print(pot.type)
# print(pot.color)
# print('#####################')
# print("Plate")
# print(plate.material)
# print(plate.type)
# print(plate.color)


# calling methods

# This will change color of the pot and only pot
# here self is passed automatiaclly, its the reference of pot here that is passed as self by default
pot.set_color("Reddish")


# print("Pot After\n")
# # print("Pot")
# print(pot.material)
# print(pot.type)
# print(pot.color)
# print('#####################')
# print(plate.material)
# print(plate.type)
# print(plate.color)


print(pot)
