
import sys
import time
import os
from colorama import Fore, init
import numpy as np

init(autoreset= True)

slow = 2.5
dia = 0.07
quick = 0.01
step = 1

from ETS_functions import *
from ETS_intro import *
from ETS_rooms import *


########################################################################################################################
########################################################################################################################
## Start of Escaping Toro Sanctum script ###############################################################################
########################################################################################################################
########################################################################################################################


print()
time.sleep(step)
header()
print("\n")
#time.sleep(step)
fast_text("\n\n\t Esacping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations,\n\
events, and incidents are products of the authors and co-authors (you, the user) imagination. Any resemblance to actual persons, both\n\
living or dead, or actual events is purely coincidental")
print("\n\n")
time.sleep(step)

#### Setting global variables and gathering user info #######################################
#############################################################################################

print("Before we begin, we need complete you character profile. Please answer the following questions\n")
pause()
class Player:
    def __init__(self, user_name, user_color, user_weight, user_item, bravo_leader, user_city, user_country):
        self.user_name = user_name
        self.user_color = user_color
        self.user_weight = user_weight
        self.user_item = user_item
        self.bravo_leader = bravo_leader
        self.user_city = user_city
        self.user_country = user_country

###collecting user input to be called later.
def get_user_input():
    user_name = (input("What is your name, Team Leader?:\n").title())
    user_color = "red"
    user_weight = input_weight("\nIn lbs, how much do you weigh?:\n")
    user_item = input("\n Of the following, which item would you choose to carry with you? \n\
    [Select 1, 2, or 3 then press <enter> ]\n\n\
    1) A lucky coin\n\
    2) A golden locket\n\
    3) A bronze compass\n")
    if user_item == "1":
        user_item = "A lucky coin"
    elif user_item == "2":
        user_item = "A golden locket"
    elif user_item == "3":
        user_item = "A bronze compass"
    else:
        user_item = "empty"
    bravo_leader = "Lt. Macdonald"
    user_city = "Jekyll"
    user_country = "USA"
    return(Player(user_name, user_color, user_weight, user_item, bravo_leader, user_city, user_country))
##using user class with calling input
ETS_user = get_user_input()

starting_question(ETS_user)
print("\n\n")
header()
print("\n\n\n\n\n")

introduction(ETS_user)

pause()

escaping_sanctum(ETS_user)
