# Error Handling

# print(name)

# keywords involved:
# try
# except
# finally
# else
# raise

try:
	name = "Lets Code Together"
	print(name)
except Exception as e:
	# print("name is not defined")
	print(e)
finally: # this always run regardless of fail case
	print("FInally to the end")


try:
	# name = "Lets Code Together"
	print(name)
except Exception as e:
	# print("name is not defined")
	print(e)
else: # it runs if there is no error in the try block
	print("Else Worked")

# Exception is the base class of builtin errors. This is used when we dont know what the eror type can be


# NameError
# this occurs if ther variable is not defined

try:
	print(name)
except NameError as e:
	print(e)
	print("name is not defined")


# TypeError

print(1 + "abc")

try:
	print(1 + "abc")
except TypeError as e:
	print(e)


# KeyError

dict1 = {1: "One"}
try:
	print(dict1[2])
except KeyError as e:
	print(f"{e} is missing")


# print(1/0)

# Handling Multiple Errors

num1 = 10
try:
	num2 = int(input("Enter a number to divide 10 with: "))
	print(num1/num2)
except (ZeroDivisionError, ValueError) as e:
	# print(e)
	print(type(e).__name__) # what is the type
	print(e) # what the error is


# # error case
num1 = 10
try:
	num2 = int(input("Enter a number to divide 10 with: "))
	print(num1/num2)
except (ZeroDivisionError, ValueError) as e:
	# print(e)
	print(type(e).__name__) # what is teh type
	print(e) # what the error is
finally:
	print(10/num2)


working case
num1 = 10
try:
	num2 = int(input("Enter a number to divide 10 with: "))
	print(num1/num2)
except (ZeroDivisionError, ValueError) as e:
	# print(e)
	print(type(e).__name__) # what is teh type
	print(e) # what the error is
else:
	print(10/num2)


# to raise an exception from our side
def run():
	num1 = int(input("Enter a number: "))

	if num1 == 0:
		# raise ZeroDivisionError("0 is Invalid")
		raise Exception("Zero is not valid")

try:
	run()
except Exception as e:
	print(e)
