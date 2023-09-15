# 1. What is list
       # 0  1  2  3  4    5
arr = [1, 2, 3, 4, 5, "Lets Code Together"]
print(arr)
print(type(arr))


# # 2. Accessing, appending and removing

# # Accessing

print(arr[0])

print(f"The second element is: {arr[1]}")

print(f"The last element is: {arr[-1]}")

print(f"The 2nd last element is: {arr[-2]}")



# # Append / Insert

arr.append(6)
print(f"The new list is: {arr}")

arr.insert(0, 100)
print(arr)

# # pop

arr.pop()
print(F"After pop: {arr}")

arr.pop(0)
print(arr)




# 3. What is slicing

# name_of_list[start: end]   start is included not end
list[start: end: step]

# [1, 2, 3, 4, 5 ,6]


# new_list = arr[1:5]
# print(new_list)


after_1 = arr[1:]
print(after_1)


# print(arr)
# print(arr[0::2])

print(arr[::-1]) # v-imp


# 4. For Loop and multi dimension
arr = [1, 2, 3, 4, 5, "Lets Code Together"]

for elem in arr:
	print(elem)


# x = range(10)
# print(type(x))

range(start:end:step)

# for number in range(0, 10, 2):
# 	print(number)

multi_dim = [[1,2,3], [4,5,6]]

# 1 2 3
# 4 5 6
# print(len(multi_dim))

# for row in range(len(multi_dim)):
# 	for col in range(len(multi_dim[0])):
# 		print(multi_dim[row][col], end = " ")
# 	print("\n")


# 5. sort, reverse

arr = [1, 2, 3, 4, 5, "Lets Code Together"]

arr.reverse()
print(arr)


nums = [2, 3, 6, 8, 0]

nums.sort(reverse=True)
print(nums)



# 6. Push to Github

