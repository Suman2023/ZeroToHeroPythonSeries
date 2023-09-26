# what is import?
# importing functionality from other scripts (python file)

# import module
# from module import add

# print(add(5,5))

# print(module.__name__)
# print(module.add(5,6))
# print(module.x)

# https://docs.python.org/3/library/math.html
# import math

# print(math.pi)

# print(math.cos(90))


# https://docs.python.org/3/library/datetime.html
# import datetime
# from datetime import datetime

# # now()

# print(datetime.now())



# from datetime import datetime

# def time_log(func):
# 	def wrapper(*args, **kwargs):
# 		start_time = datetime.now()
# 		func(*args, **kwargs)
# 		end_time = datetime.now()
# 		print(f"Time taken for {func.__name__}: {end_time - start_time}")
# 	return wrapper

# @time_log
# def return_num():
# 	list1 = list()
# 	for i in range(50000000):
# 		list1.append(i)
# 	for num in list1:
# 		pass

# def return_num_gen():
# 	for i in range(50000000):
# 		yield i

# @time_log
# def call_generator():
# 	list1 = return_num_gen()
# 	for num in list1:
# 		pass


# return_num()
# call_generator()


# where does python look for packages when importing
# import sys

# print(sys.path)



# https://pypi.org/
# https://requests.readthedocs.io/en/latest/
# import requests


# python = requests.get("https://python.org")
# print(python)
# print(python.text)

# response = requests.get("https://ipinfo.io")
# print(response.json())



# Fun packages

# import this


# import antigravity

# import webbrowser as wb

# wb.open("https://python.org")

# look at eg: letscodetogether.py
# import turtle


# tt = turtle.Turtle()

# tt.shape("turtle")

# tt.pensize(30)

# tt.forward(200)

# tt.right(90)

# tt.forward(100)

# tt.right(90)

# tt.forward(200)

# tt.right(90)

# tt.forward(100)

# tt.circle(100)


# turtle.done()


# https://tkdocs.com/tutorial/index.html
# tkinter (for creating GUI)
# look at eg: subscribe.py



