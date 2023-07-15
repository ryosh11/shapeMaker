import turtle 

t = turtle.Turtle()

def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def rectangle():
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)

def circle():
    t.circle(100)

def triangle():
    t.forward(100) 
    for i in range(2):
        t.left(120)
        t.forward(100)

def rhombus():
    t.left(45)
    t.forward(100)
    for i in range(3):
        t.left(90)
        t.forward(100)

def star():
    for i in range(5):
        t.forward(100)
        t.right(144)

name = input("What shape should I draw. ")
if name == "square":
    square()
elif name == "rectangle":
    rectangle()
elif name == "triangle":
    triangle()
elif name == "circle":
    circle()
elif name == "rhombus":
    rhombus()
elif name == "star":
    star()
