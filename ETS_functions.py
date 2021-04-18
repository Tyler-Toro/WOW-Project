'''
ETS Functions
'''
import sys
import time
import os
import numpy as np

slow = 2.5
dia = 0.1
quick = 0.01
step = 1


def input_weight(weight):
    while True:
        try:
            userInput = int(input(weight))
        except:
            print("This is not a whole number, please try again")
            continue
        else:
            return userInput
            break


def pause():
    pausing = input("\n  press <enter> to continue...\n")

def slow_text(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(quick)
    time.sleep(dia)

def fast_text(text, delay = quick):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(quick)

def storyline_paragraph(text):
    for line in text.split("\n"):
        print(line, flush = True)
        time.sleep(quick)
    time.sleep(quick)

def starting_question(ETS_user):
    start_esaping_sanctum = input(f"{ETS_user.user_name}, would you like to Start? (Y/N):\n")
    if start_esaping_sanctum == "n" or start_esaping_sanctum == "N":
        print("Game Over. Please reload program")
        sys.exit()
    elif start_esaping_sanctum == "y" or start_esaping_sanctum == "Y":
        pass
    else:
        print("that was not a valid response.")
        starting_question(ETS_user)

def header():
    storyline_paragraph("  \t\t   .... ............... ..........................\n\
  \t\t   .. ......................... .......... .......\n\
  \t\t   ...... ..... ......... ........................\n\
  \t\t   .........  Escaping Toro Sanctum...... ........\n\
  \t\t   ........ ............... ............... ......\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")


