#importing

import sys
import time
import os
import numpy as np

#functions

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
    

    #print(door_hp)
    #else:
        #print("You have broken through the door!!! Now plant the explosi")



hit_door_hp()
#print("You have broken through the door!!! Now plant the explosives")   