from numpy import *
import pygame as pyg
'''
We would use the numpy to for random enemy spawning or attacking and pygame for effects, just thought I would make some enemy classes for a room which for now is the armory but we can always just import enemy class functions from here also.
'''

class User:
    	def __init__(self):
		self.hp = 25
		self.maxhp = 50
		self.dmg = 3

#upgrades to user and user health variables.  
upg = 0
hpupg = 0
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
    				if User.upg == 0:
					enemy_class = random.choice([Zombie, Dead_Team_Member, Wild_Dog])
				else:
					enemy_class = random.choice([Zombie, Dead_Team_Member, Wild_Dog])

				enemy = enemy_class()
				enemy_name = enemy_class.__name__

				print(f"You encounter a {enemy_name}! (A to attack)")

				enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

				while enemy.hp > 0 or User.hp > 0:
					print("Press A to attack")
					user = input().lower()

					if user != "a" and user != "y":
						print("Please enter a valid action")
						continue

					if user == "a":
						enemy.hp = enemy.hp - User.dmg
						print(f"You dealt {User.dmg} damage to the {enemy_name}!")

					if enemy.hp <= 0:
						print("You have slaughtered {enemy_name}!")
						battle = False