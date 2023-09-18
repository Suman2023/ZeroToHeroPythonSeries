# # 1. length of list

# arr = [1, 2, 3, 4, 5, 6]
# length = len(arr)
# print(f"The length of arr: {length}")


# # 2. remove item

# arr.pop(0) # here 0 is the index
# print(arr)


# arr.remove(3)  # here 3 is not an index but an element
# print(arr)

# # 3. delete
#        # 0  1  2  3
# arr = [1, 2, 3, 4, 5, 6]

# del arr[1:3]
# print(arr)


# del arr[0]
# print(arr)

# del arr[:]
# print(arr)

# # 4. clear
# print(f"Before: {arr}")

# arr.clear()

# print(f"AFTER: {arr}")

# # 5. index


# arr = [1, 2, 3, 4, 5, 6]

# index = arr.index(2)
# print(f"The index of 2 is {index}")


# index = arr.index(1000)  # 1000 should be in the list to work
# print(index)

# # 6. count

# arr = [ 1, 2, 1, 3, 4, 4, 4]

# count = arr.count(1)  # here 1 is not index but the element
# print(f"The number of times 1 appear in the list is : {count}")

# count_4 = arr.count(4) 
# print(f"The number of times 4 appear in the list is : {count_4}")


# count_100 = arr.count(100) 
# print(f"The number of times 100 appear in the list is : {count_100}")


# # 7. copy (very imp)

arr1 = [1, 2, 3, 4, 5]
arr2 = arr1

# print(arr1)
# print(arr2)
# print(" ################# ")

# arr2[0] = 100
# print(arr1)
# print(arr2)

arr3 = arr1.copy()

print(id(arr1))
print(id(arr2))

print(id(arr3))




# arr2[0] = 100
# arr3[1] = 55

# print(arr1)
# print(arr2)
# print(arr3)


# # 8. enumerate

#         # 0  1  2  3   4
arr = [ 1, 6, 8, 10, 12]

for num in arr:
	print(num)

for tuple in enumerate(arr):
	print(tuple)


for index, num in enumerate(arr):
	print(index, '->', num)


# # 9. extend

# arr = [1, 2, 3, 4, 5]
# arr2 = [100, 200]


# arr3 = arr + arr2
# print(arr3)


# arr.extend(arr2)
# print(arr)



# # 10. zip

# arr1 = [1, 2, 5, 6, 7]
# arr2 = [3, 4, 5, 9, 10]

# for num1, num2 in zip(arr1, arr2):
# 	print(num1, num2)


# arr3 = [100, 200]

# for num1, num2 in zip(arr2, arr3):
# 	print(num1, num2)



# # 11. list comprehension

# square = []

# for i in range(10):
# 	square.append(i*i)
# print(square)  # 0, 1, 4, 9 ...



# square = [ i * i for i in range(10)]
# print(square)


# even = [i  for i in range(10) if i % 2 == 0]

# even = [i  if i % 2 == 0 else 'NO' for i in range(10)]

# print(even)


# 12. Github
