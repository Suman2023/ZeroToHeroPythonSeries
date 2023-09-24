import turtle
from time import sleep

wn = turtle.Screen()

wn.setup(width=1920, height=1080)  # Adjust the width and height as needed

wn.bgcolor("black")
# Create a turtle
t = turtle.Turtle()

# # Set the starting position to the top-left corner

def start_pos(margin_x=0,margin_y=0):
	t.penup()  # Lift the pen (no drawing)
	t.goto(-wn.window_width() / 2 + 380 + margin_x, wn.window_height() / 2 - 200 - margin_y)  # Set to the top-left corner
	t.pendown()  # 
	
start_pos(margin_x = 280)
t.pensize(30)
t.pencolor("#FF9933")
t.shape("turtle")

t.speed("fast")

def letter_space():
	t.penup()
	t.forward(40)
	t.pendown()

def custom_space(space):
	t.penup()
	t.forward(space)
	t.pendown()

sleep(5)

# L
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)

letter_space()

# E
for i in range(2):
	t.forward(100)
	t.backward(100)
	t.left(90)
	t.forward(75)
	t.right(90)
t.forward(100)

letter_space()

# T
t.forward(100)
t.backward(50)
t.right(90)
t.forward(150)
t.left(90)

custom_space(90)

t.left(90)
t.penup()
t.forward(150)
t.pendown()

t.backward(40)
t.right(180)
custom_space(110)
t.left(90)
custom_space(60)


# S

t.forward(100)
t.left(90)
t.forward(75)
t.left(90)

t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(100)


t.pencolor("white")
# next Line
start_pos(margin_x= 280,margin_y = 200)
#C

t.forward(100)
t.backward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)


letter_space()


# 0
for i in range(4):
	t.forward(150)
	t.left(90)
t.forward(150)

letter_space()


# D
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)

letter_space()

# E
for i in range(2):
	t.forward(100)
	t.backward(100)
	t.left(90)
	t.forward(75)
	t.right(90)
t.forward(100)

letter_space()

# next Line
start_pos(margin_y=400)

t.pencolor("green")
# # T
t.forward(100)
t.backward(50)
t.right(90)
t.forward(150)
t.left(90)

custom_space(90)


# 0
for i in range(4):
	t.forward(150)
	t.left(90)
t.forward(150)

letter_space()


# G
t.left(90)
t.forward(150)
t.right(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(75)
t.left(90)
t.forward(50)
t.right(180)
t.forward(50)


t.right(90)


custom_space(75)
t.left(90)
letter_space()


# E
for i in range(2):
	t.forward(100)
	t.backward(100)
	t.left(90)
	t.forward(75)
	t.right(90)
t.forward(100)

letter_space()

# # T
t.forward(100)
t.backward(50)
t.right(90)
t.forward(150)
t.left(90)

custom_space(90)

# H

t.left(90)
t.forward(150)
t.right(180)
t.forward(75)
t.left(90)
t.forward(100)
t.left(90)
t.forward(75)
t.right(180)
t.forward(150)
t.left(90)

letter_space()


# E
for i in range(2):
	t.forward(100)
	t.backward(100)
	t.left(90)
	t.forward(75)
	t.right(90)
t.forward(100)

letter_space()


t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(180)
t.forward(150)
t.left(180)
t.forward(75)
t.goto(t.xcor() + 100, t.ycor() -75)


t.right(90)
custom_space(80)
t.left(90)

# box

t.pencolor("red")
def box():
	t.forward(700)
	t.left(90)
	t.forward(1300)
	t.left(90)
	t.forward(900)
	t.left(90)
	t.forward(1300)
	t.left(90)
	t.forward(200)
box()
t.speed("slowest")

t.penup()
for i in range(100):
	box()
t.pendown()


turtle.done()
