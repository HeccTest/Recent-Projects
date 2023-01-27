import turtle # turtle library: https://docs.python.org/3/library/turtle.html
import time
import random

tim = turtle.Turtle()
tim.speed(0)

def example():
    # source: https://replit.com/@ritza/python-turtle#main.py
    sides = 3
    colors = ['red', 'yellow', 'orange']

    for x in range(360):
        tim.pencolor(colors[x % sides])
        tim.forward(x * 3 / sides + x)
        tim.left(360 / sides + 1)
        tim.width(x * sides / 200)

def square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)

def triangle():
    for i in range(3):
        tim.forward(100)
        tim.left(120) # 180 degrees - 60 degrees

def pentagon():
    for i in range(5):
        tim.forward(100)
        tim.left(72) # 360 degrees / 5 sides

def star():
    tim.pencolor("orange")
    tim.forward(100)
    for i in range(5):
        tim.right(72)
        tim.forward(100)
        tim.left(144)
        tim.forward(100)
# This is more so a math problem
# angles of my triangle are based on this: http://proofsfromthebook.com/wp-content/uploads/2013/08/pentagram2.png

def ff(): # this is for fun, make any pattern
    tim.penup()
    tim.goto(-350, 350)
    tim.pendown()
    tim.screen.colormode(255)

    xCord = -350 # going toward down
    yCord = 350 # going toward right
    size = 700
    for i in range(101):
        turtleColour = (190 - i, i * 2, 150 + i) # arbitrarily changes colour
        tim.pencolor(turtleColour)
        tim.penup()
        tim.goto(xCord + i * 7, yCord - i * 7)
        tim.pendown()
        for j in range(4):
            tim.forward(size)
            tim.right(90)
        size -= 14

def ff2(): # for fun 2
    yScreen = 350
    for j in range(8):
        tim.penup()
        tim.goto(-350, yScreen - ((j - 1) * 100))
        tim.pendown()  
        tim.pencolor("blue")

        tim.right(60)
        for i in range(7):
            tim.forward(100)
            tim.left(120)
            tim.forward(100)
            tim.right(120)

        tim.penup()
        tim.goto(-350, yScreen - ((j - 1) * 100) - 100)
        tim.pendown()
        tim.pencolor("red")

        tim.left(120)
        for i in range(7):
            tim.forward(100)
            tim.right(120)
            tim.forward(100)
            tim.left(120)
        tim.right(60)
        tim.width(j)

def maze():
    tim.penup()
    tim.goto(-350, 350)
    tim.pendown()
    tim.pencolor("orange")

    # 4 sides, 700px per side. make one entrance, one exit (50px wide?)
    entrance = random.randint(1,4) # entrance will be a random side (1 to 4)
    correctExit = random.randint(1,4) # exit path
    while(correctExit == entrance):
        correctExit = random.randint(1,4) # regenerate exit until not same as entrance
    for i in range(4):
        if(entrance == i):
            path = random.randint(0, 650)
            tim.forward(path)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.forward(650 - path)
        elif(correctExit == i):
            path = random.randint(0, 650)
            tim.forward(path) # go forward a random amount (between 0 and 650)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.forward(650 - path)
        else:
            tim.forward(700)
        tim.right(90)

    print(entrance)
    print(correctExit)

def run():
    tim.penup()
    tim.goto(-350,200)
    tim.pendown()
    square()

    tim.penup()
    tim.goto(-150,200)
    tim.pendown()
    triangle()

    tim.penup()
    tim.goto(50,200)
    tim.pendown()
    pentagon()

    tim.penup()
    tim.goto(-350,0)
    tim.pendown()
    star()


# example()
# run()
# ff()
# ff2()
maze()
# turtle.clearscreen()
input("Press Enter")