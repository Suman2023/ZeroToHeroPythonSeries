# Handling Files in Python

# open(path_of_file, mode)
# mode: read(r), write(w), append(a)


# reading
# # the file needs to exist, doesn't create if not exist
# file = open("logfile.txt", "r")

# # print(file.read()) # reads the complete file

# # print(file.readline()) # reads one line

# #print(file.readlines()) # puts all lines in a list

# file.close()


# write
# creates a file if not exist
# if exist it will clear the file content(v. imp)
# file = open("logfile.txt", "w")

# file.write("This was written using Python")

# file.close()


# append
# doesn't clear teh content if file exist
# creates the file if not exist

# file = open("logfile.txt", "a")

# file.write("\nWritten using Python")

# file.close()


# position

# file = open("logfile.txt", "r")

# print(file.tell())  # gives current position


# file.seek(5)  # takes the cursor to the given position

# print(file.tell())


# file.close()


# opening file in multiple mode
# r+ -> opens in read and write
# w+ -> write and read mode
# a+ -> append and read mode

# file = open("logfile.txt", "a+")

# file.seek(8)

# text = file.read()

# replacemt = "a " + text

# file.write(replacemt)

# text = file.read()
# print(text)

# file.close()



# Updating files 

# file = open("logfile.txt", "r+")

# file.seek(8)

# text = file.read()  # this takes the pointer to the end of file

# file.seek(8)

# replacemt = "a " + text

# file.write(replacemt)


# file.close()




# Better way to open and handles files
# recommended

# with open("logfile.txt", mode="r") as file:
# 	lines = file.readlines()
# 	for line in lines:
# 		print(line)


	

