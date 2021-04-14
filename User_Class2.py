class user:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        self.inventory = {}
    def setName(self, name):
        self.name = name
    def addToInventory(self, k, v):
        self.inventory[k] = v
def start():
    weight = int(input("Enter your weight: "))
    name = input("Enter your name: ")
    player = user(weight, name)
    alternanateName = input("Do you want to change you name: ")
    player.setName(alternanateName)
    return player
def room(user):
    if user.weight > 200:
        print(player.name + " Fell to through the floor")
    else:
        print(player.name + " Walks up to the safe")
player = start()
room(player)