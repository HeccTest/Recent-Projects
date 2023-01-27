import turtle
import random
import time

turtles = [] # array holding all of our turtles

line = turtle.Turtle() # setting up a finish line
line.penup()
line.goto(100, 0) # the win condition is for a turtle to have their xcor() > 100, therefore the finished line should be at x = 100
line.color("violet") # I like violet
line.pendown()
line.left(90)
line.forward(220)
line.write("FINISH LINE")
line.hideturtle() # hides the arrow. any written text or the trail drawn remains

for i in range(10): # setup; turtle generation
    turtles.append(turtle.Turtle()) # add a new turtle to the end of the list [0 - 9]
    turtles[i].speed(10)
    turtles[i].penup() # no drawing while moving

    r = random.randint(0, 255) # set a random red value
    g = random.randint(0, 255) # set a random green value
    b = random.randint(0, 255) # set a random blue value
    turtles[i].screen.colormode(255) # default rgb values accepted is the range of 0 to 1.0. This changes that to be 0 to 255
    turtles[i].color((r, g, b)) # set turtle at index i to the colour rgb generated above

    turtles[i].goto(-400, 200 - (i * 20)) # spaces out each turtle
    turtles[i].pendown()
    turtles[i].forward(10)


playing = True
startTime = time.time() # record the start time
while (playing == True):
    for turtle in turtles:
        turtle.forward(random.randint(0,30))

        if turtle.xcor() > 100: # finished line at x = 100, we start at x = -400
            playing = False
            turtle.write("I won in: " + str(round((time.time() - startTime), 2)) + " S")
            # str casts our rounded float into a string. 
            # round(number, digits). round our number (end time - start time) to 2 decimal places
            break # breaks out of the if loop ensuring the turtles underneath do not move after someone wins


time.sleep(100) # janky fix for screen closing on code completion