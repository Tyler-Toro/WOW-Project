############### importing ############

import sys
import time
import os
import numpy as np
import random

slow = 2.5
dia = 0.1
quick = 0.01
step = 1

############# functions ##############


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
        time.sleep(quick)
    time.sleep(quick)


def basement_header():
    storyline_paragraph("  \t\t   .... ............... ..........................\n\
  \t\t   .. ......................... .......... .......\n\
  \t\t   ...... ..... ......... ........................\n\
  \t\t   .........  Escaping Toro Sanctum ...... ........\n\
  \t\t   ........ ..... The Basement ............ ......\n\
  \t\t   ::::::::::::::::....      .....:::::::::::::::::::\n\
  \t\t   :::::::::::::::::::::.  .::::::::::::::::::::\n\n\n")


rng = np.random.default_rng()

roof_access = "".join([str(x) for x in rng.integers(10, size =4)])

'''
def pause():
    pausing = input("\n  press <enter> to continue...\n") #need to add one for the breaking 
    # the door "press enter to punch the door" and add it to door_hp

def door_damage():
    damaging = input("\n  press <enter> to break the door...\n")

'''


'''
# def wrong_choice_option():
#     print("Wrong choice, Please Try again!!!")
#     starting_question()
#     print()
#     get_lever_direct()
we did not use
'''

'''
def hit_door_hp(door_hp = 20):
    while door_hp > 0:
        door_damage()
        door_hp = door_hp - 5
        if door_hp != 0:
            print(f"You have weakened the door down to {door_hp}% of its strength") #figure out how to remove zero from the if statement print out %
        else:
            print(f"WARNING!!! Failure!!! WARNING Door is it at {door_hp}%. You have broken through the door!!! Now plant the explosives")
    return door_hp

def get_lever_direct():
    lever_direct = ["left", "right", "up", "down"]
    elavator_stop = False
    lever_input = input("Which direction do you want to pull the lever?")
    pause()
    random_choice = random.choice(lever_direct)
    print(f"You chose '{lever_input}''.The correct choice was '{random_choice}'.")
    
    if random_choice == lever_input: # having issue here with catching the wrong random string and entering into the apprpriate loop. Using while asking user input and checking while they dont have it right. line 177 in rooms on main branch
        elavator_stop = True
        basement_fork()
    else:
        basement()

 use these already       
 '''       


# def starting_question():
#     start_esaping_sanctum = input("Player 1, would you like to Start? (Y/N):\n").lower()
#     if start_esaping_sanctum == "n":
#         print("Game Over. Please reload program")
#         sys.exit()
#     elif start_esaping_sanctum == "y":
#         pass
#     else:
#         print("that was not a valid response.")
#         starting_question()

'''
def electrical_room():
    hit_door_hp() ###need to finish story###
    #basement_unitA(EST_user)
'''

'''
# def boiler_room():
#     temperature = 65
#     # add word degrees

#     while temperature < 115: # randomize key cards and letters and define and call key list
#         for key in boiler_keys:
#             print(keys)
#         user_key = input("\n\nWhat key do you want try:  \n").lower()
#         if user_key == "B":
#             storyline_paragraph("\nThe decontamination chamber doors open and oxygen is pumped back into the room.\n") # add boiler story
#             break
#         else:
#             temperature += 20
#             boiler_keys.remove(user_key)
#             storyline_paragraph(f"{ETS_user.user_name}\'s notices there is a WARNING ALARM for inceasing temperature.\n")
#             slow_text("\"The Door is Still Locked\"\n\n")
#     if temperature == 115:
#         storyline_paragraph("The Room is engulfed in flames!!!!\n")
#         slow_text("\tYou the burned the Alpha Team!!! Game Over\n\n")
#         retry = input("Try again? (Y/N)\n").lower()
#         if retry == "n" or retry == "N":
#             sys.exit()
#         elif retry == "y" or retry == "Y":
#             time.sleep(step)
#             escaping_sanctum(ETS_user)
#         else:
#             time.sleep(step)
#             print("\t\tInvalid response".upper())
#             lab(ETS_user)

# boiler_keys = ["A","B","C"]

****...added this to the story already...****
'''



'''
# def basement_fork():
#     basement_input = input(" What direction will you take Team Alpha? \n\
# [Select 1 or 2, then press <enter> ]\n\n\
# 1) Right: \'Boiler Room\'\n\
# 2) Left: \'Electrical Power System\'\n")

#     if basement_input == "1":
#     # time.sleep(step)
#     # basement_room()
#         print("you are in the boiler room")
#         boiler_room()
#     elif basement_input == "2":
#     # time.sleep(slow)
#         print("you are the the electrical room")
#         electrical_room()
#     else:
#         print("\n\t\tinvalid response".upper())
#         time.sleep(step)
#         print("\n\n")
#         wrong_input_basement_fork() #go back to lobby

#put this in the actual file aready
'''
################ class ###################

# class temperature:
#     def __init__(self, temperature, decrease):
#         self.temperature = temperature
#         self.decrease = decrease

# def get_input_temp():
#     temperature = (input("What is the room temperature?:\n")

#     decrease = self.temperature - 10


'''

create a class to get the temp

room temp attribute decrease temp
git temp metod amd lower __init__ to give intial temp
temp = 80
return temp

get_temp
    self.temp=80
    decrease = self.temp - 5

'''

#game starts at this point
#broke everything down to functions and calls

basement_header() #1 
'''
(Alpha Team heads out the freight elevator that leads to the basement)
((It's been hours since they have heard anything from Bravo Team))
{ETS_user.user_name} yells,")

                #slow_text 
                "WE NEED TO FIND THEM AND GET THE HELL OUT OF HERE
'''

starting_question() #2

'''
(player leaves main lobby and enter the freight elevator that goes to the basement)
(player encounter a situtation where the elavator malfunctions....the rope snaps)


'''
get_lever_direct() #3

basement_fork() #4

'''
Boiler Room
(There is a WARNING ALARM for was a what appears to be a pipe that burst)
(the zombies have must have damaged control unit which has caused damage to the pipes)
(Alpha Team knows that they must head to the boiler room in order to stop the leak)
(Alpha team must turn off the pipeline line)
'''

# get_input_temp() #5


