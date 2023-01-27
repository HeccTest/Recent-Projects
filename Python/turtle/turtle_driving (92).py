import turtle
import time
import random

tim = turtle.Turtle()
tim.shape("turtle") # changes our turtle's shape, other variations are: arrow, turtle, circle, square, triangle, classic
tim.color("violet")
window = turtle.Screen()

speed = 10
turnSpeed = 15
score = 0 # this is a global variable, but it has to be redefined to be used in a function

coin = turtle.Turtle()
coin.color("orange")
coin.width(10)
coin.shape("circle")
coin.penup() # the coin will not have a trail

coin.goto(random.randint(-500, 500), random.randint(-300, 300)) # go to random x y coordinate

def coinCollision():
    global score # score is a global variable and usable by the function coinCollision()
    if tim.distance(coin) < 10:
        score += 1
        print("Score: " + str(score))
        coin.goto(random.randint(-500, 500), random.randint(-300, 300))
        if score > 4: # win condition
            window.bye() # closes the turtlegraphics window, effectively ending the game
            print("you win")


def moveForward():
    tim.forward(speed) # makes tim the turtle move forward by a fixed amount of pixels indicated by speed
    coinCollision()

def moveBackward():
    tim.backward(speed)
    coinCollision()

def turnLeft():
    tim.left(turnSpeed)
    coinCollision()

def turnRight():
    tim.right(turnSpeed)
    coinCollision()

window.onkeypress(moveForward, "Up") # when the key "Up" is pressed run the function moveForward
window.onkeypress(moveBackward, "Down")
window.onkeypress(turnLeft, "Left")
window.onkeypress(turnRight, "Right")

window.listen() # listens to key-events (ie. key press by the user)
window.mainloop() # starts event loop (effectively an infinite loop to continually listen for events)

# time.sleep(100)