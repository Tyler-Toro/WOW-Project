'''
Game text, add to storyline, see flow below

Escaping Toro Sanctum:


\\\\User questions:

Before we begin, we need complete you character profile. Please answer the following questions:

- What is your name, Team Leader?:
- In lbs, how much do you weigh?
- What is your favorite color?
- Of the following, which item would you choose to carry with you?
    [Select 1, 2, or 3 then press <enter> ]
    1) A lucky coin
    2) A golden locket
    3) A bronze compass

- Who is someone you look up to or are inspired by?
- Name a city you would like to travel to someday
- Finally, what is a country you are least likely to travel to?


\\\\Game Start:
    input(f"{user_name}, would you like to Start? (Y/N)


\\\\Intro:
A single flash of lightning casts dozens of long shadows across the skybridge. The subsequent
thunder crashes, deafening the small group. The rain is relentless, making the view in every direction a
grey abyss. The only feature made out in the distance, as another flash of lightening blazes across the sky,
is the outline of a gigantic building. An entire team has been missing from the rendezvous for the better
part of an hour. Someone is shouting over the rain, gripping a radio...

-{user_name}): \"....-repeat, Systems check! Over!
......
-{user_name}): \"...Systems check, come in Team Bravo!
...(radio silence)...
....<<<static>>>
- {user_name}): \"BRAVO, DO YOU READ???!!!
...(radio silence)...
- {user_name}): \"Damn!! Alpha, move out!

Rain continues to pour in sheets as Alpha team scans the lobby of Toro Sanctum, a newly constructed
bioengineering facility on {user_city.title()} Island. After the \"Incindent\", the paramilitary contractors of PiThon were
flown in from {user_country.title()} to inspect Toro Sanctum and the surrounding coast. Team Bravo led the expedition
into the facility while Team Alpha scanned the ports of entry and docks. There was nothing. No signs of anyone
having visited or worked in the high tech research facility which celebrated its launch two weeks ago. No ships
No vehicles on the newly paved parking lots. Nothing. Team Alpha lost communication with Bravo squad just as the
storm starting picking up. With limited visibility, Team Alpha rushes past the deserted security gates and double
pane glass doors of Toro Sanctum. The lobby is a massive cavern of steel and glass, abandoned and dimly lit. The rain
drums on the glass overhead as Team Alpha steps further into the facility...

\\\\Game Start 2nd & Retry 

Will you search for Bravo Team and Escape Toro Sanctum? (Y/N)


\\\\Main Path

Alpha team continues onward, moving past the lobby. The polished linoleum floors reflect each movement.
The dim emergency lights flicker, drawing the attention of the team. The rain becomes more faint as they
reach the elevator and staircase section at the end of the empty lobby
There is a sudden muffled sound that freezes {user_name} in their tracks

...<<distant radio static>>..
- {user_name}): \"Team Alpha! Hold, I hear something..
.......
..<<static>>..
(???):  ..\"hel-\"..
{user_name}): \"Its coming from the elevator shaft...


\\\\Main Path Break - Elevator, Lab, Basement

What will you do next?
    [Select 1, 2, or 3 then press <enter> ]
    1) Use the main stairs and search the basement?
    2) Head towards the emergency exit through the lab?
    3) Rappel down the elevator shaft?


    \\\\Elevator - Option 3
{user_name} leads the Team towards the center elevator and peers into the slightly opened doors
{user_name}): \"Thats a long way down...hook me up to that safety latch. I'm going down. Cover me
After securing the tactical rope, {user_name} slowly makes their decent.."
Once inside the poorly lit elevator shaft, a small sign comes into view..
f"WARNING: MAXIMUM WEIGHT FOR LATCH {(int(user_weight)-20)} LBS...
"       SNAP!"
"Game over. Try again? (Y/N):


\\\\ Labratory - Option 2

Alpha Team begins to make their way out of the area when a sudden rumble is felt...
_._.._...............::::::::::::;;;;;;;;;;;;;;;;;;;;######################<CRASH>!!!!!!!!!
All at once an elevator car comes screeching past the center shaft, coming to a crash many floors below
{user_name}): \"WHAT IS GOING ON HERE?!
{user_name.title()} peers over the ledge, then regroups the team and heads down a large corridor.
Onward, Alpha Team can see flashing {user_color.title()} lights through the large glass doors of the lab.
The laboratory doors slide against a gritty floor. The lab is field of broken glass and smoke
{user_color.title()} light is scattered in every direction as the team moves toward the emergency exit
The emergency exit doors are blocked by a mountain of large boxes, lab equipment, and garbage

user_item == "A lucky coin" or user_item == "A golden locket" or user_item == "A bronze compass":
        t3 = f"{user_item} falls out of {user_name}\'s pocket and rolls towards the lab entrance, making it to the corridor

{user_name}): \"...strange..

    \\\\ Lab Fork 

    what will you do next?
    [Select 1 or 2, then press <enter> ]
    1) Onward: \'Dig out emergency exit
    2) Go back: \'Return to lobby and take stairs to basement


    \\\\ Lab - Game Over
    The Team begins unblocking the emergency exit doors. The massive equipment pieces take
    the entire team to move aside. Shards of glass fall off of repositioned boxes. Something
    "catches {user_name}\'s eye.
    Among the glass are pieces of shredded clothing and hair
    ............................
    {user_name}): \"...WAIT....ALPHA TEAM FALL BAC------
    The exit doors plunge open. Alpha team is bombarded, surrounded in seconds
    Game Over. Try again? (Y/N)

    \\\\Lab - Return to Basement Option
    {user_name} guides Alpha Team back to the lobby and to the entrance of the main stairway


\\\\ Basement - Option 1

Alpha Team heads toward the frosted glass doors that lead to the stairs, the basement a dozen flights down
With a slight push of the doors, radio static can be fainlty heard emanating from below
{user_color.title()} lights illuminate ascending and decending steps, but the team heads towards the noise..

{user_name}): \"We need to recon with Bravo and figure out what happened here. Maybe the storm is interf-
!!!!ffffffffffffffffffffffffffffssssssssssssssssssssssssssssssssshhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!

Every piece of radio equipment on Team Alpha bursts into noise, echoing throughout the landings above
{user_name}): \"What the-- Comms off, turn comms off! ..We're going deaf and blind at this point"

There are no sounds but footsteps. Team Alpha reaches the basement level, where {user_name} finds a radio on the ground
The lost radio is badly damaged, with deep grooves scratched into the surface. But the battery pack is missing....
There is a directory on the wall

    \\\\ Basement Fork
    {user_name}, what direction will you take Team Alpha?
    [Select 1 or 2, then press <enter> ]
    1) Right: \'Freezer Section: Unit B
    2) Straight: \'Dry Storage: Unit A

    \\\\Option 1 - Unit B, Freezer
    Team Alpha makes a right and heads towards the frozen storage. The flickering {user_color} lights overhead
    crack and blink as they approach the freezer door. Through the icy window, there is a blinking LED light glowing
    on the ground in the darkness. The LED light is the same as on everyone\'s radio.
    {user_name} grasps the frozen handle and pulls the door open slowly...taking a small step inside.
    Just as {user_name} grabs the lost radio, a hand lunges out of the darkness, grabbing their wrist
    {user_name}): ...\"What th--!
    The freezer door slams shut, several locks forced in place.
    The slowing flash LED light tints the faces engulfing {user_name}...
    Game Over
    Try again? (Y/N)

    \\\\ Option 2 - Unit A, Storage
    Team Alpha continues slowly down the corridor towards the storage bay. The staircase lights become less and less
    useful with each step as they head further into darkness. The only thing visible in the distance is a small
    window hovering on the door of Storage Unit A. The dim {user_color} light creeping through is barely visible, but the shadow
    of a figure flashes past..
    {user_name} quickens their step and readies Alpha Team to breach the door
    {user_name}): \"On my mark\"..(motions)...3         2          1         
    "            BANG!
    Behind the Storage A doors lies Bravo Team. Some are injuried but all are accounted for
    {bravo_leader}): \"You look spooked, but aren\'t we glad to see you, {user_name}
    {user_name}): \"You don\'t look so hot either. Come on, let\'s get out of this place

    END:
    Both teams return to the surface using a freight elevator. The shore where they left their boats is
a ruin of vegetation and sand. The hum of engines roar over the sound of waves crashing against the vehicles. An
injured Bravo squad member peers into the greycast sky, their hand covering a curious wound on their arm......
a deep bite wound. The outline of Toro Sanctum is reflected off their gaze as they look back at the shrinking island

Thank you for playing