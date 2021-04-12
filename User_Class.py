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
    print(player.name)
    print(player.weight)
start()