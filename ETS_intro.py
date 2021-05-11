from ETS_battles import *
from ETS_functions import *
###importing from our functions file

def introduction(ETS_user):
    storyline_paragraph("\n\nA single flash of lightning casts dozens of long shadows across the skybridge. The subsequent\n\
thunder crashes, deafening the small group. The rain is relentless, making the view in every direction a grey abyss.\n\
The only feature made out in the distance, as another flash of lightening blazes across the sky, is the outline \n\
of a gigantic building. An entire team has been missing from the rendezvous for the better part of an hour.\n\
Someone is shouting over the rain, gripping a radio...\n\n")
##### calling our user class ETS_user
#####slow text effect for print statements    
    pause()
    slow_text(f"\n\t({ETS_user.user_name}): \"....-repeat, Systems check! Over!\"\n")
    slow_text("\n......\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"...Systems check, come in Team Bravo!\"\n")
    slow_text("\n...(radio silence)...\n")
    slow_text("\n....<<<static>>>\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"BRAVO, DO YOU READ???!!!\"\n")
    slow_text("\n...(radio silence)...\n")
    slow_text(f"\n\t({ETS_user.user_name}): \"Damn!! Alpha, move out!\"\n\n")
    time.sleep(slow)
    storyline_paragraph(f"\nRain continues to pour in sheets as Alpha team scans the lobby of Toro Sanctum, a newly constructed \n\
bioengineering facility on {ETS_user.user_city.title()} Island. After the \"Incindent\", the paramilitary contractors of PiThon were \n\
flown in from {ETS_user.user_country} to inspect Toro Sanctum and the surrounding coast. Team Bravo led the expedition \n\
into the facility while Team Alpha scanned the ports of entry and docks. There was nothing. No signs of anyone \n\
having visited or worked in the high tech research facility which celebrated its launch two weeks ago. No ships. \n\
No vehicles on the newly paved parking lots. Nothing. Team Alpha lost communication with Bravo squad just as the \n\
storm starting picking up. With limited visibility, Team Alpha rushes past the deserted security gates and double \n\
pane glass doors of Toro Sanctum. The lobby is a massive cavern of steel and glass, abandoned and dimly lit. The rain \n\
drums on the glass overhead as Team Alpha steps further into the facility...")
    
    time.sleep(1)
    print("\n")
