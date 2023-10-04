# Special methods  a.k.a dunder methods (double underscore)

# __init__
# __str__
# __repr__


class ABC:
    # This functions runs automatiacly while creating an instance/object from the class
    # This is mainly used for setting variable or doing some initialization
    def __init__(self):
        # print("__init__")
        self.name = "Lets Code Together"

    def run(self):
        print("RUN")

    # Not formal
    # We mainly write what teh class is suppose to do
    def __str__(self):
        return "Instance of class ABC"

    # Formal
    # This is mainly used for debugger
    def __repr__(self):
        return "ABC()"


# abc = ABC()
# # abc.run()

# print(abc)

# Doing Arithemetic

# __add__
# __sub__

# __mul__

# real + imaginary
# x =  a + ib
#  y = c + id
# x + y
# (a+c) + i(b+d)


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # print(vars(self)) # This print all the variable in the object
        # print(vars(other))
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)


cmplx1 = ComplexNumber(10, 5)
cmplx2 = ComplexNumber(20, 10)
cmplx3 = ComplexNumber(30, 15)
# self +  other = self + other
# result = cmplx1 + cmplx2 + cmplx3
result = cmplx1 - cmplx2

# print(result)
print(f"{result.real} + {result.imag}i")


# x = [1, 2, 3, 4, 5]
# print(len(x))

# __len__


class MyList:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def __len__(self):
        return len(self.words)


list1 = MyList()
list1.add("Hello")
list1.add("There")
list1.add("!")
print(list1)

print(len(list1.words))

print(len(list1))


for i in range(10):
    print(i)

# __iter__
# __next__


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration


range1 = MyRange(0, 10)

for i in range1:
    print(i)


#  __getitem__
# __setitem__


dict1 = {"1": "One"}

print(dict1["1"])  # this is using getitem

dict1["2"] = "Two"  # this is useing setitem

print(dict1)


class MyDict:
    def __init__(self):
        self.numbers = {}

    def __setitem__(self, key, value):
        self.numbers[key] = value

    def __getitem__(self, key):
        return self.numbers[key]

    def __str__(self):
        # print(self.numbers)
        return f"{self.numbers}"


dict1 = MyDict()
# print(dict1)


dict1.numbers["1"] = "One"

print(dict1.numbers)

dict1["1"] = "One"
print(dict1["1"])
