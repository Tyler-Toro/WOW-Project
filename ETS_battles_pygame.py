import sys
from ETS_functions_pygame import *
from pygame_utilities import *


class Zombie:
    def __init__(self):
        self.hp = 6
        self.dmg = 2
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def zombie_battle(ETS_user):
    zombie = Zombie()
    while zombie.hp > 0 and ETS_user.hp > 0:
        write('A zombie is attacking you!', sleep = slow)
        user_input = ask('Press A and then Enter to attack the zombie!\n>>>', (10, 350), fill = False).lower()
        if user_input == 'a': 
            zombie.update_health(ETS_user.dmg * -1)
            write(f"You have shot and dealt {ETS_user.dmg} damgage to the zombie", sleep = slow)
        ETS_user.update_health(zombie.dmg * -1)
        if zombie.hp <= 0:
            break
        text_slowmo(f"The zombie lunges at you and deals {zombie.dmg} damage !!", (5, 350), fill = False)
        
    
    if ETS_user.hp <= 0:
       write('You were killed by a Zombie, Game Over!', sleep = slow)
       sys.exit()
    else: 
        text_slowmo('You have defeated the zombie! ',(5, 300))
        
class Dead_team_member:
    def __init__(self):
        self.hp = 15
        self.dmg = 5
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def Dead_team_member_battle(ETS_user):
    dead_team_member = Dead_team_member()
    while dead_team_member.hp > 0 and ETS_user.hp > 0:
        user_input = input('Press A and then Enter to attack the dead team member!\n>>>').lower()
        if user_input == 'a': 
            dead_team_member.update_health(ETS_user.dmg * -1)
            slow_text(f"You have shot and dealt {ETS_user.dmg} damgage to the dead team member")
        ETS_user.update_health(dead_team_member.dmg * -1)
        slow_text(f"You have been dealt {dead_team_member.dmg} damage by the dead team member")
        
    
    if ETS_user.hp <= 0:
       slow_text('You were killed by a dead team member, Game Over!')
       sys.exit()
    else: 
        slow_text('You have defeated the dead team member!')