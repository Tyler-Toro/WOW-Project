#importing

import sys
import time
import os
import numpy as np
import random

slow = 2.5
dia = 0.1
quick = 0.01
step = 1

#functions


def slow_text(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(quick)
    time.sleep(dia)

def fast_text(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(quick)
    time.sleep(quick)

def storyline_paragraph(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(step)
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

def basement_header():
    storyline_paragraph("  \t\t   .... ............... ..........................\n\
  \t\t   .. ......................... .......... .......\n\
  \t\t   ...... ..... ......... ........................\n\
  \t\t   .........  Escaping Toro Sanctum ...... ........\n\
  \t\t   ........ ......The Basement............. ......\n\
  \t\t   ::::::::::::::::.............:::::::::::::::::::\n\
  \t\t   :::::::::::::::::::::.....::::::::::::::::::::\n\n\n")


rng = np.random.default_rng()

roof_access = "".join([str(x) for x in rng.integers(10, size =4)])


def pause():
    pausing = input("\n  press <enter> to continue...\n")

def hit_door_hp(door_hp = 20):
    while door_hp > 0:
        pause()
        door_hp = door_hp - 5
        if door_hp != 0:
            print(f"You have weakened the door down to {door_hp}% of its strength") #figure out how to remove zero from the if statement print out %
        else:
            print(f"WARNING!!! Failure!!! WARNING Door is it at {door_hp}%. You have broken through the door!!! Now plant the explosives")
    return door_hp

def get_lever_direct():
    elavator_stop = False
    if random_choice == lever_input: # having issue here with catching the wrong random string and entering into the apprpriate loop.
        elavator_stop = True
    else:
        print("Wrong Choice try again")
        hit_door_hp


def starting_question():
    start_esaping_sanctum = input("Player 1, would you like to Start? (Y/N):\n")
    if start_esaping_sanctum == "n" or start_esaping_sanctum == "N":
        print("Game Over. Please reload program")
        sys.exit()
    elif start_esaping_sanctum == "y" or start_esaping_sanctum == "Y":
        pass
    else:
        print("that was not a valid response.")
        starting_question()

#game starts at this point

basement_header()

starting_question()


lever_input = input("Which direction do you want to pull the lever?")

lever_direct = ["left", "right", "up", "down"]

random_choice = random.choice(lever_direct)
print(random_choice)

get_lever_direct()

basement_fork = input(f" What direction will you take Team Alpha? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Right: \'Boiler Room: Unit B\'\n\
    2) Straight: \'Electrical Power System : Unit A\'\n")

if basement_fork == "1":
    time.sleep(step)
    basement_unitB(ETS_user)
elif basement_fork == "2":
    time.sleep(slow)
    basement_unitA(ETS_user)
else:
    print("\n\t\tinvalid response".upper())
    time.sleep(step)
    print("\n\n")
    basement(ETS_user)
        
#print(lever_direct)

