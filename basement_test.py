############## Basement choice ###############################################
##############################################################################
##############################################################################

'''
notes for 4/13/2021 at 1:30am:

# need to add the color of the alarm
# need to create code that randomized the decision for elevator stopping lever
# need to finish the story that alpha team player is going to the basement to escape zombies and be freed from santum
the player must over come their fears before they reach their goal.

#will be importing "random" library to generate random idicies from a list of directions for the stop level
if correct lever is selected access to the basement, else give user two options (go to main lobby area, or quit game)
    lever_direct = ["left", "right", "up", "down"]
    
    get_lever_direct = random.choice(lever_direct)
    print(get_lever_direct)

#put ASCII where color is on line  and need to make ascii file 

#create boiler room temperate control room 

# create zombie

room temp attribute decrease temp
git temp metod amd lower __init__ to give intial temp
temp = 80
return temp

get_temp
    self.temp=80
    decrease = self.temp - 5








'''

                                    ##### next section to work on ######


'''
(player leaves main lobby and enter the freight elevator that goes to the basement)
(player encounter a situtation where the elavator malfunctions....the rope snaps)
(player faces a challenge to stop the elavator from falling but pulling the emegercy brake)
                
                lever_direct = ["left", "right", "up", "down"]
    
                get_lever_direct = random.choice(lever_direct)
        
                print(get_lever_direct)

        If successfully stopped the elevator the player makes it to the basement, else the player fails
        and has go back to main lobby, after second try game over...

***Story after successfully stopping the elavator***

(Alpha Team heads out the freight elevator that leads to the basement)
((It's been hours since they have heard anything from Bravo Team))
{ETS_user.user_name} yells,")

                #slow_text 
                "WE NEED TO FIND THEM AND GET THE HELL OUT OF HERE

(There is a WARNING ALARM for was a what appears to be a pipe that burst)
(the zombies have must have damaged control unit which has caused damage to the pipes)
(Alpha Team knows that they must head to the boiler room in order to stop the leak)
(Alpha team must turn off the pipeline line)

(stop the zombie from chewing on the electical power system)
 # winning function to call
 # use temp puzzle as for roof puzzle 

'''
### ********* Basement Header ************ ###

basement_header

    ##### Both choices 1&2 fork off in basement #########################################
    #################################################################################

basement_fork()


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