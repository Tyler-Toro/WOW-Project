
import sys
import time
import os
import numpy as np

slow = 2.5
dia = 0.1
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
slow_text("\n\n\t Esacping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations,\n\
events, and incidents are products of the authors and co-authors (you, the user) imagination. Any resemblance to actual persons, both\n\
living or dead, or actual events is purely coincidental")
print("\n\n")
time.sleep(step)

#### Setting global variables and gathering user info #######################################
#############################################################################################

print("Before we begin, we need complete you character profile. Please answer the following questions\n")
pause()
user_name = (input("What is your name, Team Leader?:\n").title())
user_weight = input_weight("\nIn lbs, how much do you weigh?:\n")
user_color = "red"
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

print()
bravo_leader = (input("Who is Team Bravo Leader?:\n").title())
user_city = "Jekyll"
user_country = "USA"
slow_text("\n...saving data....\n")  

starting_question(user_name)
print("\n\n")
header()
print("\n\n\n\n\n")

introduction(user_name, user_city, user_country)

pause()

escaping_sanctum(user_name, user_weight, user_color, bravo_leader, user_item)
