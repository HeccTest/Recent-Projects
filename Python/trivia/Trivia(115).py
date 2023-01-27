import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from playsound import playsound
playsound('intro.wav')
# import questions

# print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "WELCOME! To my Trivia game...")

# print("Time to test your knowledge!\n")
# audio.play_file('intro.wav')

# name = input("Please enter your trivia name:\n")
# print("Hello, " + name + "\n")
# time.sleep(1)
# print(colorama.Style.DIM + "Let's find out what you know and what you don't...")
# time.sleep(2)
# os.system('clear')


# print("Get ready " + name + "!")
# print("The quiz is about to begin in...")
# time.sleep(1)
# print(3)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(1)
# time.sleep(1)
# print(colorama.Back.GREEN + "Start!")
# audio.play_file('start.wav')
# time.sleep(1)
# os.system('clear')


# score = 0
# while True:
#   print(colorama.Style.DIM + questions.question1)
#   print(questions.options1)
#   answer=input()
#   if answer == questions.answer1:
#     audio.play_file('correct.wav')
#     print(colorama.Fore.GREEN + 'Correct!')
#     time.sleep(1)
#     score += 1
#     break
#   elif answer != questions.answer1:
#     audio.play_file('wrong.wav')
#     print(colorama.Fore.RED + 'Wrong! Try again')
#     time.sleep(1)
#     score -=1
#     continue

# while True:
#   print(colorama.Style.DIM + questions.question2)
#   print(questions.options2)
#   answer=input()
#   if answer == questions.answer2:
#     audio.play_file('correct.wav')
#     print(colorama.Fore.GREEN + 'Correct!')
#     time.sleep(1)
#     score += 1
#     break
#   elif answer != questions.answer2:
#     audio.play_file('wrong.wav')
#     print(colorama.Fore.RED + 'Wrong! Try again')
#     time.sleep(1)
#     score -=1
#     continue

# while True:
#   print(colorama.Style.DIM + questions.question3)
#   print(questions.options3)
#   answer=input()
#   if answer == questions.answer3:
#     audio.play_file('correct.wav')
#     print(colorama.Fore.GREEN + 'Correct!')
#     time.sleep(1)
#     score += 1
#     break
#   elif answer != questions.answer3:
#     audio.play_file('wrong.wav')
#     print(colorama.Fore.RED + 'Wrong! Try again')
#     time.sleep(1)
#     score -=1
#     continue

# audio.play_file('finish.wav')
# print(colorama.Style.BRIGHT + "Congratulations are in order!" +colorama.Style.NORMAL+ " You have finished the quiz.")
# print("You got a total score of " + colorama.Back.MAGENTA + str(score))
# if score >= 1:
#   print("You know your stuff!")
# elif score == 0:
#   print("So close!")
# else:
#   print("Better luck next time!")

# time.sleep(2)