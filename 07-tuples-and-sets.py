# 1. What is tuple?
# ordered immutable collection of data

tup = (1, 2, 3, "Lets Code Together")

print(tup)
print(type(tup))


# for single element
tup1 = (1)  # this is not tuple
print(tup1)
print(type(tup1))

tup1 =  (1,)
print(tup1)
print(type(tup1))


# 2. access elements

print(tup[-1])


a, b, c, d  = tup  # unpacking

print(a)
print(b)
print(c)
print(d)

# 3. loop over tuple

for elem in tup:
	print(elem)

# 4. mutability

# once created cannot be modified

tup[0] = 12

tup2 = tup + (1,2,3)
print(tup2)



# 5. different from list


# its immutable -> it cannot be modified once created
# it used parenthesis for formation


# 6. What is set?
 unordered mutable unique element collection -> means it has no indexing

s = { 1, 2, 3}


print(s)
print(type(s))


# 7. add and remove

s.add(5)
print(s)
s.add(5)
print(s)


s.remove(1)
print(s)

s.remove(6)  # not possible since the element doesnot exist
print(s)


# 8. union
# unique clubbing

s1 = {1 , 2, 2, 4}
s2 = {1, 5, 7}

# ans = { 1, 2, 4, 5, 7}

ans = s1.union(s2)
print(ans)



# 9. intersection
# common among collections

s3 = {1, 5, 8}
s4 = {7, 0, 5}

# ans = {5}

ans = s3.intersection(s4)
print(ans)




# 10. differenec
# it prints the differnece between two collevtion i.e which exist in one but not in another
s5 = {1, 4, 7}
s6 = {4, 7}

ans = s5.difference(s6)
print(ans)



# 11. Push to github






