from numpy import *
class Zombie:
	def __init__(self):
		self.hp = 6
		self.dmg = 2

class Dead_Team_Member:
	def __init__(self): 
		self.hp = 15
		self.dmg = 5

class Wild_Dog:
	def __init__(self):
		self.hp = 3
		self.dmg = 1
 # not sure how to tie in the battle variable... 
while battle == True:
    if Ets_User == 0:
					enemy_class = random.choice([Zombie, Dead_Team_Member, Wild_Dog])
				else:
					enemy_class = random.choice([Zombie, Dead_Team_Member, Wild_Dog])

				enemy = enemy_class()
				enemy_name = enemy_class.__name__

				print(f"You encounter a {enemy_name}! (A to attack)")

				enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

				while enemy.hp > 0 or Ets_User.hp > 0:
					print("Press A to attack")
					ETS_User = input().lower()

					if ETS_User != "a" and user != "y":
						print("Please enter a valid action")
						continue

					if ETS_User == "a":
						enemy.hp = enemy.hp - ETS_User.dmg
						print(f"You dealt {ETS_User.dmg} damage to the {enemy_name}!")

					if enemy.hp <= 0:
						print("You have slaughtered {enemy_name}!")
						battle = False