# 1. lambda func

# is a "small", "anonymous" function defined using the
# "lambda" keyword

# def is_even(num):
# 	return num % 2 == 0

# lambda variable,... : exression

# even = lambda num: num % 2 == 0

# print(is_even(2))
# print(even(2))

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(is_even, list1)))

# print(list(filter(lambda num : num % 2 == 0, list1)))

# print(list(map(lambda num: num ** 2 , list1)))














# 2. generators

# is a special type of function that allows you to create iterators in a more memory-efficient and lazy-evaluationmanner

# best usecase
# the task involves a long list or long processing so its better to break into chunks


# def return_number(num):
# 	list1 = list()
# 	while num < 100000000:
# 		list1.append(num)
# 		num += 1
# 	return list1
# print(return_number(0))

# lst = return_number(0) # this returns list
# print(lst[0])

# generators uses the keyword: yield
# def return_number_gen(num):
# 	while num < 100000000:
# 		yield num
# 		num += 1
# print(return_number_gen(0))

# for i in return_number_gen(0):
# 	print(i)
# 	if i == 100:
# 		break

# gen_fun = return_number_gen(0)

# print(next(gen_fun))
 # cannot use index












# 3. decorators

# special type of function to modify behavior of an 
# existing function or method without changing its source code


# define a function and pass the function as an 
# argumnet.. here log is the function, func is the arg


# here func is the function which will get modified

# define a wrapper function that will have all the modification inside the function here log.

# finally return the wrapper function.

# to use the decoration use '@' symbol folowed by decoration function name  above the original function


def log(func):
	def wrapper(*args, **kwargs):
		# before function call
		print(f"Calling Log for {func.__name__}")
		print(args, kwargs)

		# function call
		result = func(*args, **kwargs) # this is where the actuall function runs

		# after function call
		print(f"After computation the result: {result}")
		return result
	return wrapper
		


# @log
# def add(num1, num2):
# 	result = num1 + num2
# 	return result

@log
def sub(num1, num2):
	return num1 - num2

print(sub(2,3))

