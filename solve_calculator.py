# Variables and Input

# print("Sum")
# number1 = int(input("Enter 1st Number: "))
# number2 = int(input("Enter 2nd Number: "))
# print(f"The sum of {number1} and {number2} is {number1 + number2}")

# print("Subtraction")
# number1 = int(input("Enter 1st Number: "))
# number2 = int(input("Enter 2nd Number: "))
# print(f"The difference of {number1} and {number2} is {number1 - number2}")




# Conditonal Statement

# number1 = int(input("Enter 1st Number: "))
# operator = input("Enter the opeartor (+, -, *, /): ")
# number2 = int(input("Enter 2nd Number: "))

# if operator == "+":
# 	print(f"The sum of {number1} and {number2} is {number1 + number2}")
# elif operator == "-":
# 	print(f"The difference of {number1} and {number2} is {number1 - number2}")
# else:
# 	print("To be implemneted") # Homework



# Loops
should_continue = True
while should_continue:
	number1 = int(input("Enter 1st Number: "))
	operator = input("Enter the opeartor (+, -, *, /): ")
	number2 = int(input("Enter 2nd Number: "))

	if operator == "+":
		print(f"The sum of {number1} and {number2} is {number1 + number2}")
	elif operator == "-":
		print(f"The difference of {number1} and {number2} is {number1 - number2}")
	else:
		print("To be implemneted")

	option = input("Should I continue? (Y/N): ")

	if option == "Y":
		continue # go back to cond
	else:
		should_continue = False
	
