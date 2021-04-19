from ETS_functions import *
import sys

def escaping_sanctum(ETS_user):
    escaping_sanctum0 = input("\nWill you search for Bravo Team and Escape Toro Sanctum? (Y/N)\n")
    if escaping_sanctum0 == "n" or escaping_sanctum0 == "N":
        print("Understood\n")
        time.sleep(step)
        slow_text("Game Over")
        sys.exit()
    elif escaping_sanctum0 == "y" or escaping_sanctum0 == "Y":
        main_lobby(ETS_user)
    else:
        print("This isn\'t a valid response. Try again:\n")
        escaping_sanctum(ETS_user)


def main_lobby(ETS_user):
    slow_text("\n\t\t\t __Main Lobby__\t\n\n")
    storyline_paragraph(f"\nAlpha team continues onward, moving past the lobby. The polished linoleum floors reflect each movement. \n\
The dim emergency lights flicker, drawing the attention of the team. The rain becomes more faint as they reach the elevator and \n\
staircase section at the end of the lobby. The empty elevator shafts are hollowed silos extending in each direction. There is \n\
a sudden muffled sound that freezes {ETS_user.user_name} in their tracks\n")
    pause()
    slow_text("\n\n...<<distant radio static>>..\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"Team Alpha! Hold, I hear something..\"\n")
    slow_text("\n.......\n")
    slow_text("\n..<<static>>..\n")    
    slow_text(f"\n(???):  ..\"hel-\"..\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"Its coming from the elevator shaft...\"\n\n")
    escaping_sanctum2 = input("\nWhat will you do next?\n\
    [Select 1, 2, 3, or 4 then press <enter> ]\n\n\
    1) Use the main stairs and search the basement?\n\
    2) Head towards the emergency exit through the lab?\n\
    3) Climb the stairs to the roof access point?\n\
    4) Rappel down the elevator shaft?\n")
    if escaping_sanctum2 == "1":
        time.sleep(quick)
        basement(ETS_user)
    elif escaping_sanctum2 == "2":
        time.sleep(quick)
        lab(ETS_user)
    elif escaping_sanctum2 == "3":
        time.sleep(quick)
        roof(ETS_user)
    elif escaping_sanctum2 == "4":
        storyline_paragraph(f"\n{ETS_user.user_name} leads the Team towards the center elevator and peers into the darkness below")
        slow_text(f"\n\t({ETS_user.user_name}): \"Thats a long way down...hook me up to that safety latch. I'm going down. Cover me\"\n")
        storyline_paragraph(f"\nAfter securing the tactical rope, {ETS_user.user_name} slowly makes their decent..\n\
Once inside the poorly lit elevator shaft, a small sign comes into view..\n")
        pause()
        slow_text(f"\n\nWARNING: MAXIMUM WEIGHT FOR LATCH {(int(ETS_user.user_weight)-20)} LBS...\n")
        storyline_paragraph("       SNAP!\n")
        header()
        retry = input("Game over. Try again? (Y/N):\n")
        if retry == "n" or retry == "N":
            sys.exit()
        else:
            escaping_sanctum(ETS_user)
    else:
        print("Invalid response")
        time.sleep(step)
        main_lobby(ETS_user)




############## Basement choice ###############################################
##############################################################################
##############################################################################

def basement(ETS_user):
    slow_text("\n\t\t\t __Basment__ \t\n\n")
    storyline_paragraph(f"\n\nAlpha Team heads toward the frosted glass doors that lead to the stairs, the basement many flights down. \n\
With a slight push of the doors, radio static can be fainlty heard emanating from below. {ETS_user.user_color.title()} lights illuminate ascending \n\
and decending steps, but the team heads towards the noise..\n")
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
    slow_text("\n\t\t\t __Basement: Unit A__\t\n\n")
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
    slow_text("\n\t\t\t __Basement: Unit B__\t\n\n")
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



############## Lab Choice ##########################################
####################################################################
####################################################################

def lab(ETS_user):
    slow_text("\n\t\t\t __Laboratory__\t\n\n")
    storyline_paragraph("\n\nAlpha Team begins to make their way towards the sealed glass doors of the laboratory wing.\n\
The powerless automatic doors are pushed open with ease as Team Alpha enters the decontamination area. There is a sudden rumble felt...\n\
From many levels below comes the sound of heavy machinery and gears slowly grinding to a halt.")
    slow_text(f"\n\t({ETS_user.user_name}): \"What is going on here? It sounds like someone..\"\n")
    storyline_paragraph(f"\n{ETS_user.user_name} peers back towards the lobby as the decontamination doors lock into place. Alpha Team can see flashing\n\
{ETS_user.user_color.title()} lights overhead as the air is slowly pulled out of the room.\n")
    pause()
    slow_text(f"\n\t({ETS_user.user_name}): \"We have to shut this damn thing down!\"\n")
    storyline_paragraph(f"\nNear the wall is an emergency shut off switch, with wires exposed. {ETS_user.user_name} rushes over to examine the switch\n")
    cuts = 0
    #print(correct_wire.upper())
    while cuts < 3:
        for wire in wires:
            print(wire)
        user_wire = input("\n\nWhat color wire will you cut:  \n")
        if user_wire == correct_wire:
            storyline_paragraph("\nThe decontamination chamber doors open and oxygen is pumped back into the room.\n")
            break
        else:
            cuts += 1
            wires.remove(user_wire)
            slow_text("\nBeep......beep.....beep....\n")
            slow_text("\"nothing happened\"\n")
    if cuts == 3:
        storyline_paragraph(f"{ETS_user.user_name}\'s vision becomes blurry as the room reaches 0% oxygen level, coughing, Team Alpha falls to the ground\n")
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
            lab(ETS_user)
    storyline_paragraph(f"\nTeam Alpha stumbles on while catching their breath. The cooridor to the Lab is empty and appears untouched. The laboratory doors \n\
slide against a gritty floor. The lab is field of broken glass and debris. {ETS_user.user_color.title()} light is scattered in every direction as the team \n\
moves toward the emergency exit. The emergency exit doors are blocked by a mountain of large boxes, lab equipment, and garbage\n")
    pause()
    if ETS_user.user_item == "A lucky coin" or ETS_user.user_item == "A golden locket" or ETS_user.user_item == "A bronze compass":
        slow_text(f"{ETS_user.user_item} falls out of {ETS_user.user_name}\'s pocket and rolls out of the lab entrance, making it to the corridor\n")
        time.sleep(slow)
        slow_text(f"\n\t({ETS_user.user_name}): \"...strange..\"\n\n")
    else:
        pass

    lab_fork = input(f"{ETS_user.user_name}, what will you do next? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Onward: \'Dig out emergency exit\'\n\
    2) Go back: \'Return to lobby and take stairs to basement\'\n")
    if lab_fork == "1":
        time.sleep(step)
        lab_onward(ETS_user)
    elif lab_fork == "2":
        time.sleep(slow)
        lab_flee(ETS_user)
    else:
        print("\n\t\tinvalid response".upper())
        time.sleep(step)
        print("\n\n")
        lab(ETS_user)

#### Lab option A - Game over          ##############################
#####################################################################

def lab_onward(ETS_user):
    slow_text("\n\t\t\t Laboratory: Emergency Exit \t\n\n")
    storyline_paragraph(f"\nThe Team begins unblocking the emergency exit doors. The massive equipment pieces take the \n\
entire team to move aside. Shards of glass fall off of repositioned boxes. Something catches {ETS_user.user_name}\'s eye.\n")
    pause()
    storyline_paragraph("\nAmong the glass are pieces of shredded clothing and hair\n\n")
    slow_text(".............................\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"......WAIT....ALPHA TEAM FALL BAC------\n")
    storyline_paragraph("\nThe exit doors plunge open. Alpha team is bombarded, surrounded in seconds\n")
    header()
    retry = input("Game Over. Try again? (Y/N)\n")
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        print("\n\t\tInvalid response".upper())
        lab_onward(ETS_user)


### Lab option B - Chance to return to lobby ###############################################
############################################################################################

def lab_flee(ETS_user):
    storyline_paragraph(f"\n{ETS_user.user_name} guides Alpha Team back to the lobby and to the entrance of the main stairway\n")
    basement(ETS_user)


### Roof Choice ##########################################################
##########################################################################

def roof(ETS_user):
    slow_text("\n\t\t\t __Rooftop__\t\n\n")
    storyline_paragraph(f"\n\nTeam Alpha led by {ETS_user.user_name} heads towards the staircase and starts the long climb to the roof\n\
access door. The light becomes dimmer and dimmer as they accend, the faint outline of a large metal door seems further away with each step.\n\
The sound of rain and distant thunber can be felt humming behind the steel door. The door is being held open by something... \n\
{ETS_user.user_name} reaches down and pushes the door slightly to grab the small object")
    slow_text(f"\n\t({ETS_user.user_name}): \"What is this? It looks like a small bone...\n")
    storyline_paragraph(f"\nThe Team kicks open the door and rushes the rooftop. In every direction are bullet casings and empty ammunition\n\
crates. The helicopter on the helipad is destroyed; a twisted metal skeleton with it\'s propellers folded. The AH-{(str(roof_access[0]))+(str(roof_access[1]))}\n\
Apache helicopter is military grade...The team moves further onto the roof when the metal door behind them slams shut")
    pause()
    storyline_paragraph("The door is reinforced steel with a blinking keypad above the door handle.\n")
    slow_text("\t[ _ _ _ _ ]\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"Dammit! The keypad barely has power supply.\n")
    storyline_paragraph(f"\nStill gripping the small bone, {ETS_user.user_name} feels something carved into it. There are a series of numbers but some are\n\
too difficult to make out. All that is legible is \"_ _ {roof_access[2:]}\"")
    print(roof_access)
    #print((str(roof_access[0]))+(str(roof_access[1])))
    attempt_count = 0
    while attempt_count < 3:                                      # PyTest ??
        roof_attempt = input("\n\t Enter the correct access pin:")
        if roof_attempt == roof_access:
            slow_text("\n\t<<<Access granted>>>\n\n")
            pause()
            storyline_paragraph(f"The team rushes through the door and races down the steps in growing darkness. {ETS_user.user_name} shuts the heavy\n\
door just as decayed arms and hands are within reach. The team heads straight to the basement.\n")
            basement(ETS_user)
            break
        else:
            attempt_count += 1   # PlUS EQUALS 5 HEAD
            slow_text("\n\tinvalid entry\n") 
    if attempt_count == 3:
        storyline_paragraph(f"\n\nAn alarm blares from the rooftop and echoes throughout the island. The access door keypad flashes {ETS_user.user_color}\n\
as smoke rises from the power circuit. The alarm continues on as flocks of birds scatter off of distant tree tops. As the sirens screech...a closer\n\
sound becomes audible...")
        pause()
        slow_text("..........Hrrrrrnnnnggggg....\n")
        slow_text(f"\n\t({ETS_user.user_name}): \"What the -----\n")
        storyline_paragraph(f"All at once, dozens of zombies rise up and slowly head towards team Alpha. {ETS_user.user_name} punches\n\
the access panel and shuts off the alarm system. The zombies move closer and closer to the team")
        storyline_paragraph(f"The team heads to the rooftop ledge and stares down that the concrete below. With no choice left, {ETS_user.user_name}\n\
orders the team to rappel down to the nearest window\n")
        roof_escape(ETS_user)
        

def roof_escape(ETS_user):
    storyline_paragraph(f"\nThe sound of harnesses zipping down the rappel lines buzz like a thousand angry wasps. The team soars down and lunges inside\n\
the nearest row of windows several landings below. Crashing through glass, {ETS_user.user_name} disconnects the rappel line and lands on a \n\
concrete surface. The room is dark and humid, the air acrid.\n")
    pause()
    slow_text("....................\n")
    slow_text("\n....................\n")
    slow_text(f"\n\t({ETS_user.user_name}): Something's not right in here...\"\n")
    fast_text("\n...........hhhHHHHRNNNGAAA!!!\n")
    storyline_paragraph(f"\n{ETS_user.user_name} raises a flashlight and illuminates the faces of a zombie hoard rushing toward Team Alpha..\n")
    retry = input("Game Over. Try again? (Y/N)\n")
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        print("\n\t\tInvalid response".upper())
        roof_escape(ETS_user)


## Puzzle variables ########################

rng = np.random.default_rng()

roof_access = "".join([str(x) for x in rng.integers(10, size =4)])

wires = ["red", "blue", "green", "black", "yellow", "orange"]

correct_wire = np.random.choice(wires, replace = False)

def create_string_from_int_list(intList):
    return "".join([str(x) for x in intList])
