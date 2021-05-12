import sys
from ETS_functions import *


class Zombie:
    def __init__(self):
        self.hp = 6
        self.dmg = 2
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def zombie_battle(ETS_user):
    zombie = Zombie()
    while zombie.hp > 0 and ETS_user.hp > 0:
        fast_text('\nA zombie has attacked you!\n')
        user_input = input('Press A and then Enter to attack the zombie!\n>>>').lower()
        if user_input == 'a': 
            zombie.update_health(ETS_user.dmg * -1)
            fast_text(f"\nYou have shot and dealt {ETS_user.dmg} damgage to the zombie\n")
        ETS_user.update_health(zombie.dmg * -1)
        fast_text(f"You have been dealt {zombie.dmg} damage by the zombie!\n")
        
    
    if ETS_user.hp <= 0:
       slow_text('You were killed by a Zombie, Game Over!')
       sys.exit()
    else: 
        slow_text('You have defeated the zombie!')
        
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