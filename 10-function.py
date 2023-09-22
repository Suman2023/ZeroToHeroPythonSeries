What is function?
> its a block of code to perform specific task and can be reused

l1 = ["", "Code", "Programmer"]

MAX_LENGTH = -1
WORD = ""
for word in l1:
	if len(word) > MAX_LENGTH:
		MAX_LENGTH = len(word)
		WORD = word
print(f"The maximum length is: {MAX_LENGTH} with word: {WORD}")


l2 = ["", "Code", "Programmer", "Programming")]
MAX_LENGTH = -1
WORD = ""
for word in l1:
	if len(word) > MAX_LENGTH:
		MAX_LENGTH = len(word)
		WORD = word
print(f"The maximum length is: {MAX_LENGTH} with word: {WORD}")


# How do we define a function
# keep the name that suggest what the block of code will do
# use small case, use underscrore to break words

# defination
def function_name():
	# TODO
	print("This is a function")

function_name()


def return_number():
	print("Print inside return_number")
	return 5

var = return_number()

print(return_number())
print(var)


# scope

def add():
	x = 5  # local to the func cannot be accessed outside
	y = 10
	return x + y

# result = add()
# print(result)

print(x)
print(y)


# parameters in function


def add(first, second):
	return first + second

# add() # throws error

result = add(5 , 6)
print(result)

# # named parameter

result = add(second=6, first=5)
print(result)


# solving the eg above

l1 = ["", "Code", "Programmer"]
l2 = ["", "Code", "Programmer", "Programming"]

def longest_word(word_list):
	MAX_LENGTH = -1
	WORD = ""
	for word in word_list:
		if len(word) > MAX_LENGTH:
			MAX_LENGTH = len(word)
			WORD = word
	# print(f"The maximum length is: {MAX_LENGTH} with word: {WORD}")
	return (WORD, MAX_LENGTH)

result1 = longest_word(l1)
result2 = longest_word(l2)
print(result1)
print(result2)


# impact of original
x = 5

def add_one(num):
	num += 1
	return num

y = add_one(x)


print(x)
print(y)


# immutable dpesn't change
# mutable does change

x = [1,2 ,3]

def add_one(lst):
	lst.append(4)
	return lst

y = add_one(x)

print(x)
print(y)


# default
# this is defined only once, the value is set on the defination only once


def add(first=0, second=0):
	return first + second

print(add())
print(add(5))

# caution when adding default list/dic or any mutable types
def add(lst = []):
	lst.append(1)
	return lst

print(add())
print(add())


# solutions
# copy

def add(lst = []):
	lst = lst.copy()
	lst.append(1)
	return lst

print(add())
print(add())

# using None as default for mutable type
def add(lst = None):
	if lst is None:
		lst = []
	lst.append(1)
	return lst

print(add())
print(add())

# def add(first,second)
# 	pass

# add(1, second = 5)


def func(*args, **kwargs):
	print(args)  # tuple
	print(kwargs)  # dict


# func(1,2,3,name="Lets Code Together")


# def add(first,second):
# 	return first + second


def add(*args, **kwargs):
	print(args)
	print(kwargs)
	if kwargs.get("should_break"):
		return 0
	return sum(args[:3])

print(add(1,2,3,4,5,6,should_break = False))


# Documentation


def add(first: int, second: int):
    """
    Takes two numbers add them and send the result
    """
    return first + second


print(add(1, "hello"))
