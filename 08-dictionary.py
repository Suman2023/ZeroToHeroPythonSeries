# 1. What is Dictionary/dict?

# its a Data structure which store in key-value pair where all keys are hashable and unique

# var = {key: value}

d = {"a": "Apple", "b": "Ball"}
print(d)
print(type(d))


# 2. Dict declaration and hashbility

# key : needs to be hashable
# string, int, float, tuple (element inside tuple needs to be hashable)

# not hashable: list, sets

x = hash("a")


y = hash([1,2,3]) # throws error

d2 = {1: "One", 1.5: "float", "str": "String", (1,2,3): "tuple",
 "list" : [1,2,3,4]}
# print(d2)


# 3. Accessing


print("First element: ")
print(d2[1])


# Error

print(d2[10])


print(d2.get(10))  # None if not found
print(d2.get(10, "Not Found")) 
print(d2.get(1)) 




# 4. add new item

d3 = {}

d3["key"] = "Value"

d3.update({"1": "One"})  # if not found add else update the existing


d3.update({"1": "Updated"})

d3["1"] = "Updated Again"

# print(d3)




# 5. remove items


d3.pop("1")
print(d3)




del d3["1"]
print(d3)





# 6. loop over (items, keys, values)

d4 = {"A" : "Apple", "B": "Ball"}
print(d4)

items = d4.items()
print(items)

for key, value in d4.items():
	print(key,"->", value)



keys = d4.keys()
# print(keys)

for key in d4.keys():
	print(key)


values = d4.values()
# print(values)

for value in d4.values():
	print(value)



# 7.use case (square of numbers)

# d5 = {}
# for i in range(10):
# 	d5[i] = i*i
# print(d5)

# d6 = {"Name" : "Lets Code Together", "Age" : 1}
# print(d6)





# 8. Dict comprehension

d7 = {i : i*i for i in range(10)}
print(d7)




# 9. Tip to convert two list to key value pair dict

list1 = ["A", "B", "C"]

list2 = ["Apple", "Ball", "Cat"]


tup =  zip(list1, list2)
# print(list(tup))
d8 = dict(tup)
print(d8)




# 10. Push to Github





