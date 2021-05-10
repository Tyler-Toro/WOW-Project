import sys
class Zombie:
    def __init__(self):
        self.hp = 6
        self.dmg = 2
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def zombie_battle(ETS_user):
    zombie = Zombie()
    while zombie.hp > 0 and ETS_user.hp > 0:
        print('A zombie has attacked you!')
        user_input = input('Press A and then Enter to attack the zombie!' /n).lower()
        if user_input == 'a': 
            zombie.update_health(ETS_user.dmg * -1)
            print(f"You have shot and dealt {ETS_user.dmg} damgage to the zombie")
        ETS_user.update_health(zombie.dmg * -1)
        print(f"You have been dealt {zombie.dmg} damage by the zombie!")
        
    
    if ETS_user.hp <= 0:
       print('You were killed by a Zombie, Game Over!')
       sys.exit()
    else: 
        print('You have defeated the zombie!')