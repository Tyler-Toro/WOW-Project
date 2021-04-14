############## Basement choice ###############################################
##############################################################################
##############################################################################

'''
# need to add the color of the alarm
# need to create code that randomized the decision for elevator stopping lever
# need to finish the story that alpha team player is going to the basement to escape zombies and be freed from santum
the player must over come their fears before they reach their goal.

#will be importing "random" library to generate random idicies from a list of directions for the stop level
if correct lever is selected access to the basement, else give user two options (go to main lobby area, or quit game)
    lever_direct = ["left", "right", "up", "down"]
    
    get_lever_direct = random.choice(lever_direct)
    print(get_lever_direct)

#put ASCII where color is on line 

#create boiler room

# create zombie

'''

def basement(ETS_user):
    storyline_paragraph(f"\n\nAlpha Team heads toward the freight elevator that leads to the basement. \n\
There is a WARNING ALARM for was a what appears to be a pipe that burst. {ETS_user.user_color.title()} alarm lights illuminate ascending \n\
Alpha Team knows that they must head to the boiler room in order to avoid ..\n")
    pause()
    slow_text(f"\n\n\t({ETS_user.user_name}): \"We need to recon with Bravo and figure out what happened here. Maybe the storm is interf-\n")
    slow_text("\n!!!!ffffffffffffffffffffffffffffssssssssssssssssssssssssssssssssshhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!\n")
    storyline_paragraph("\n\nEvery piece of radio equipment on Team Alpha bursts into noise, echoing throughout the landings above.")
    slow_text(f"\n\t({ETS_user.user_name}): \"What the-- Comms off, turn comms off! ..We're going deaf and blind at this point\"\n")
    storyline_paragraph(f"\nThere are no sounds but footsteps. Team Alpha reaches the basement level, where {ETS_user.user_name} finds a radio on the ground.\n\
The lost radio is badly damaged, with deep grooves scratched into the surface. But the battery pack is missing....\n\
There is a directory on the wall\n")
    pause()

    ##### Both choices 1&2 fork off in basement #########################################
    #################################################################################

    basement_fork = input(f"{ETS_user.user_name}, what direction will you take Team Alpha? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Right: \'Freezer Section: Unit B\'\n\
    2) Straight: \'Dry Storage: Unit A\'\n")
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


### Basement - choice 2 (Storage A) #########################################################
#############################################################################################


def basement_unitA(ETS_user):
    storyline_paragraph(f"\nTeam Alpha continues slowly down the corridor towards the storage bay. The staircase lights become less and less\n\
useful with each step as they head further into darkness. The only thing visible in the distance is a small window hovering on the door of \n\
Storage Unit A. The dim {ETS_user.user_color} light creeping through is barely visible, but the shadow of a figure flashes past..\n\n")
    pause()
    storyline_paragraph(f"{ETS_user.user_name} quickens their step and readies Alpha Team to breach the door.")
    slow_text(f"\n\t ({ETS_user.user_name}): \"On my mark\"..(motions)...3         2          1         ")
    storyline_paragraph("            BANG!\n")
    pause()
    storyline_paragraph("\nBehind the Storage A doors lies Bravo Team. Some are injuried but all are accounted for.")
    slow_text(f"\n ({ETS_user.bravo_leader}): \"You look spooked, but aren\'t we glad to see you, {ETS_user.user_name}\"\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"You don\'t look so hot either. Come on, let\'s get out of this place\"\n")
    pause()
    slow_text("Both teams return to the surface using a freight elevator. The shore where they left their boats is\n\
a ruin of vegetation and sand. The hum of engines roar over the sound of waves crashing against the vehicles. An\n\
injured Bravo squad member peers into the greycast sky, their hand covering a curious wound on their arm......\n\
a deep bite wound. The outline of Toro Sanctum is reflected off their gaze as they look back at the shrinking island.")
    slow_text("\n\n\t\t\t Thank you for playing\n")
    header()

### Basement - Choice 1 (Storage B) ###########################################################
###############################################################################################

def basement_unitB(ETS_user):
    storyline_paragraph(f"\nTeam Alpha makes a right and heads towards the frozen storage. The flickering {ETS_user.user_color} lights overhead \n\
crack and blink as they approach the freezer door. Through the icy window, there is a blinking LED light glowing on the ground in \n\
the darkness. The LED light is the same as on everyone\'s radio.\n")
    pause()
    storyline_paragraph(f"\n{ETS_user.user_name} grasps the frozen handle and pulls the door open slowly...taking a small step inside. Just as \n\
{ETS_user.user_name} grabs the lost radio, a hand lunges out of the darkness, grabbing their wrist\n")
    slow_text(f"\n\t({ETS_user.user_name}): ...\"What th--!\"\n")
    pause()
    storyline_paragraph(f"The freezer door slams shut, several locks forced in place.\n\
The slowing flash LED light tints the faces engulfing {ETS_user.user_name}...\n")
    header()
    slow_text("\tGame Over\n\n")
    retry = input("Try again? (Y/N)\n")
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        print("\t\tInvalid response".upper())
        basement_unitB(ETS_user)