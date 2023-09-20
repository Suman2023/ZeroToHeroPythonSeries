# 1. What are operators?

Operator are special keyword that alows you to perform Various operations in variables and values.

+, - , = ** ==, &



# 2. Various Category

Arithemtic ( +, -, * , /)
Comparision ( ==, > , < .....)
Logical (and, or, ...)
Assigment ( =, += ....)
Bitwise ( &, | ,...)
Membership (in, notin ...)
Identity ( is )





# 3.Arithmentic Operators


x = 5
y = 10


print(x+y) # add

print(x - y) # sub

print(x * y) # mul

print(y / x) # div

print(y // x) # floor div

print(2 ** 3) # 2 * 2 * 2 power


# 4. Comparison Operators

# it compares two values


x = 5
y = 10
z = 5

print( x < y)  # less then

print( x > y)   #greater then

print(x <= z) # less then or equal

print( x >= y)  # greater then or equal

print( x == y)  # equals

print( x != y) # not equals



# 5. Logical Operators

x = 0  # False
y = 1  # True


a = True
b = False

print(a and b)
print( x and y)


print( a or b)


if not x:
	print("Presnt")
else:
	print("Absent")




# 6. Assignment Operators

x = 10

print(x)


x = x + 5
print(x)

x += 5
print(x)


x -= 5
print(x)

x *= 5
print(x)


# /, //, **  (homework)




# 7.Bitwise Operator

# 0 -> 00
# 1 -> 01
# 2 -> 10
# 3 -> 11
# 4 -> 100


print(bin(4)[2:])


# and (if any one is false the result is false)

x = 4
y = 5

bin_4 = bin(4)[2:]
bin_5 = bin(5)[2:]

print(bin_4)
print(bin_5)


print(x & y)

 # 1 0 0
 # 1 0 1
 # -------
 # 1 0 0


# or  ( if any one is true the result is true)

print( x | y)

 # 1 0 0
 # 1 0 1
 # -------
 # 1 0 1


# xor ( if both are same then its false else true)
print(x ^ y)

#  1 0 0
#  1 0 1
#  -------
#  0 0 1

# left shift  ( << )

z = 4 # 100
print( z << 2)   #   1 0 0 0 0

print(bin(16))



# # right shift ( >> )

z = 4 # 100
print(z >> 2)  # 1
print(bin(1))




# 8. Membership Operator

s = "Lets Code Together"

print("c" in s)

print("L" in s)


l = [1, 2, 5]
print( 1 in l)



print(5 not in l)








# 9. Identity Operators


l1 = [1, 2, 3]
l2 = [1, 2, 3]

l3 = l2

print(l1 == l2)  # looks for value

print(l1 is l2)  # it looks for reference or memory location

print(l2 is l3)




# special case.. python stores int from -5 to 256 in cache
a = 10
b = 10

print( a == b)
print(a is b)

d = 500
e = 500
print( d == e)

print(d is e) # it can either be True or False



# 10. Push to Github
