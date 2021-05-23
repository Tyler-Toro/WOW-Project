import sys
import time
import pygame

from pygame_utilities import *

slow = 2.5
dia = 0.07
quick = 0.01
step = 1


def input_weight(user_question):
    while True:
        try:
            userInput = int(ask(user_question))
        except:
            text_wrap("This is not a whole number, please try again", (5,500), font_size = 30)
            time.sleep(slow)
            continue
        else:
            return userInput
            break




def slow_text(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(dia)
    time.sleep(dia)

def fast_text(text, delay = quick):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(dia)

def storyline_paragraph(text):
    for line in text.split("\n"):
        print(line, flush = True)
        time.sleep(step)
    time.sleep(dia)

def starting_question(ETS_user):
    start_esaping_sanctum = ask(f" {ETS_user.user_name}, would you like to Start? (Y/N): >>>")
    if start_esaping_sanctum == "n" or start_esaping_sanctum == "N":
        text_slowmo("Game Over. Please reload program", (X//2, Y//2))
        time.sleep(slow)
        sys.exit()
    elif start_esaping_sanctum == "y" or start_esaping_sanctum == "Y":
        header()
        time.sleep(slow)
    else:
        text_wrap("that was not a valid response.", (200, 450))
        starting_question(ETS_user)

def header():
    text_slowmo(".... ............... ................ ................... ....\n \
.. ......................... .......... ... ..................\n \
...... ..... ......... ............. ................... .....\n \
.........  Escaping Toro Sanctum...... ...\n \
........ ............... ............... .....................\n \
::::::::::::::::::::::::::::::::::::::::::::::::::\n \
:::::::::::::::::::::::::::::::::::::::::::::::::::",(0,10))


# save point