# all()

# a = ["", 1, 2, 3, 4, 5]
# print(all(a))

# any()

# list1 = [0, 1, 2, 3, 4, 5]
# print(any(list1))


# bin()

# print(bin(4)[2:])


# bool()


# print(bool(0))

# print(bool([]))

# print(bool(""))

# print(bool(1))

## complex()

# cmp = a + ib

# print(complex(12))

# print(complex(12, imag=5))





# dict()

# dict1 = {}

# dict2 = dict()
# print(dict2)

# dict3 = dict({"a": 1})
# print(dict3)



# dir()

# list1 = [1, 2, 3]

# print(dir(list1))

# print(dir(dict))



# divmod()


# print(divmod(10,5))

# 10/5 = 2, 10 % 5 = 0




# enumerate()

# list1 = ["Hello" , "Hi"]

# for word in list1:
# 	print(word)


# for index, word in enumerate(list1):
# 	print(index,word)





# eval()

# str1 = "2 + 2 / 5 + 7 * 8"

# print(eval(str1))




# exec()

# str2 = '''
# def run():
# 	print("This is RUN")
# run()
# '''

# exec(str2)



# filter()
# filter(func, iter)

# def is_even(num):
# 	return num % 2 == 0

# list2 = [ 1, 2, 3, 4, 5 ,6 ,7 ,8]

# print(list(filter(is_even, list2)))





# float()

# x = 10

# print(float(x))



# format()

# name = "Lets Code Together"
# when = "Today"

# print("Subscribe to {} {}".format(name,when))


# print("Subscribe to {name} {when}".format(name=name,when=when))







# frozenset()

# fset = frozenset({1,2,3})

# # fset.add(12)
# print(fset)


# getattr()

# list1 = [1, 2, 3]

# # print(dir(list1))

# getattr(list1, "append")(4)

# print(list1)


# globals()

# x = 10

# def run():
# 	return "RUN"

# y = 5


# g = globals()

# print(g)




# hasattr()

# will discuss more on class


# hash()


# list1 = [1, 2, 3]
# print(hash(list1))

# fset = frozenset({1, 2, 3})
# print(hash(fset))




# help()

# if 

# help("if")





# hex()


# print(hex(200))



# id()


# list1 = [1, 2, 3]
# list2 = list1
# x = 100

# print(id(list1))
# print(id(list2))
# print(id(x))






# input()


# name = input("Enter you name: ")
# print(name)



# int()

# print(int(10.5))

# print(int("123"))







# isinstance()

# x = 10

# print(type(x))

# print(isinstance(x, int))





# iter()


# iter1 = iter([1, 2, 3])
# # print(iter1)

# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))





# len()
# iter1 = iter([1, 2, 3])
# iter1 = [1, 2, 3]
# print(len(iter1))





# list()

# list1 = []
# print(list1)

# list2 = list()
# print(list2)







# locals()
# a = 10
# def run():
# 	x = 10
# 	y =5
# 	l = locals()
# 	print(l)


# run()







# map()

# def square(num):
# 	return num * num

# list1 = [1, 2 ,3, 4]

# list2 = list(map(square, list1))
# print(list2)







# max()

# list1 = [1 , 100, 500]

# print(max(list1))




# # min()
# print(min(list1))






# next()

# look @ iter above









# oct()


# x = 100
# print(oct(x))




# ord()



# print(ord("a"))
# print(ord("A"))

# print("A" < "a")












# pow()


# print(2 ** 3)

# print(pow(2, 3))







# print()

# print(" This is a print function ")




# range()
# range(start, end , step)

# rng = range(10)
# # print(rng)


# for i in rng:
# 	print(i)







# reversed()

# list3 = [ 1, 2, 3]
#  # [3, 2, 1]

# print(list(reversed(list3)))







# round()


# print(round(1.2))
# print(round(1.7))









# set()

# set1 = {}

# set2 = set()

# print(set1)
# print(set2)




# setattr()
# more on class lecture






# slice()

# list2 = [1, 2, 3, 4, 5]

# slc = slice(0, 3)


# print(list2[0:3]) # better
# print(list2[slc])








# sorted()

# list1 = [0, 5, 10, 11, 2, 4]


# print(list(sorted(list1)))
# print(list(sorted(list1, reverse=True)))





# str()
# x = str(123)
# print(x)
# print(type(x))








# sum()

# list5 = [1, 2, 3]

# print(sum(list5))








# tuple()


# tup1 = tuple()

# print(tup1)




# type()


# x = 12
# print(type(x))



# zip()

list1 = [1, 2, 3]
list2 = [4, 5, 6]


for num1, num2 in zip(list1, list2):
	print(num1, num2)




