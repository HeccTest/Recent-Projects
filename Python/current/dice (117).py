import random
import time
import os

dice = ["⚀","⚁","⚂","⚄","⚃","⚅"]
dice = [
"""
 =======
|       |
|   o   |
|       |
 =======
""",

"""
 =======
| o     |
|       |
|     o |
 =======
""",

"""
 =======
| o     |
|   o   |
|     o |
 =======
""",

"""
 ======= 
| o   o |
|       |
| o   o |
 ======= 
""",

"""
 ======= 
| o   o |
|   o   |
| o   o |
 =======
""",

"""
 =======
| o   o |
| o   o |
| o   o |
 =======
"""
]

# cycle through a bunch of dice (visual cinematic type thing)

def intro():
  for i in range(10):
    print(random.choice(dice)) # print a random dice
    time.sleep(0.5)
    os.system('cls') # clear screen
intro()

# prompt user to be ready (any key starts)

userIn = input("Ready to start?")

# player 1's turn (type 1, 2, or 3 to roll that dice. Any other input will not roll)

p1 = 0 # player one's score
p2 = 0 # player two's score

for i in range(6):
  print(random.choice(dice)) # print a random dice
  time.sleep(0.5)
  os.system('cls') # clear screen

os.system('cls')
rolls = []

for i in range(3): # roll three dice for p1
  rolls.append(random.choice(dice))

print(rolls[0], rolls[1], rolls[2])

for i in range(3): # p1 gets to choose what to do
  userIn = input("which dice would you like to roll? [1, 2, 3, or type anything else to skip]\n> ")
  if(userIn == "1"):
    rolls[0] = random.choice(dice) # reroll dice 1
  elif(userIn == "2"):
    rolls[1] = random.choice(dice) # reroll dice 2
  elif(userIn == "3"):
    rolls[2] = random.choice(dice) # reroll dice 3

  os.system('cls')
  print(rolls[0], rolls[1], rolls[2])

# Scoring

if(rolls[0] == rolls[1] and rolls[1] == rolls[2]):
  print("Three of a kind! Thats 30 Points!")
  p1 += 30
elif(rolls[0] == rolls[1] or rolls[1] == rolls[2] or rolls[0] == rolls[2]): 
  print("A Pair! Thats 10 Points!")
  p1 += 10
else:
  print("Unlucky, no points")

time.sleep(3)
os.system("cls")

# player two's turn

print("Player two's turn ")
time.sleep(1)
for i in range(6):
  print(random.choice(dice)) # print a random dice
  time.sleep(0.5)
  os.system('cls') # clear screen

rolls = []

for i in range(3): # roll three dice for p2
  rolls.append(random.choice(dice))

print(rolls[0], rolls[1], rolls[2])

# implement dumb CPU to play for p2 (randomly roll)

for i in range(3): # p1 gets to choose what to do
  print("which dice would you like to roll? [1, 2, 3, or type anything else to skip]\n> ", end="")
  time.sleep(random.randint(1, 5)) # fake CPU thinking time
  choice = random.randint(1,3)
  print(choice)
  time.sleep(2) # give player time to see what CPU did
  if(choice == 1):
    rolls[0] = random.choice(dice) # reroll dice 1
  elif(choice == 2):
    rolls[1] = random.choice(dice) # reroll dice 2
  elif(choice == 3):
    rolls[2] = random.choice(dice) # reroll dice 3

  os.system('cls')
  print(rolls[0], rolls[1], rolls[2])

# Scoring

if(rolls[0] == rolls[1] and rolls[1] == rolls[2]):
  print("Three of a kind! Thats 30 Points!")
  p2 += 30
elif(rolls[0] == rolls[1] or rolls[1] == rolls[2] or rolls[0] == rolls[2]): 
  print("A Pair! Thats 10 Points!")
  p2 += 10
else:
  print("Unlucky, no points")

time.sleep(3)
os.system("cls")



if(p1 > p2):
  print("Player one wins! with: " + p1 + " points")
elif(p2 > p1):
  print("Player two wins! with: " + p2 + " points")
else:
  print("Tie!")