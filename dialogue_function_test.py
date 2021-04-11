import time

def storyline(text):
    print(text)
    time.sleep(1)


time.sleep(1)
storyline("\nThis is the first line of the story")
storyline("This is the second line of the story")


long_string = "THis is a very long string to try and pring something line by line\n\
the string goes on and on for several lines and it separated by \"\ n\" so lets\n\
see if this gets printed correctly"

def storyline_paragraph(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(1)

print()
time.sleep(1)
storyline_paragraph(long_string)

time.sleep(1)
print()

name = "tyler"
age = 30

storyline_paragraph(f"THis is a very long string to try and pring something line by line\n\
the string goes on and on for several lines and it separated by \"\ n\" so lets\n\
see if this gets printed correctly\n\
Now we would like to add {name} and their age {age}. Did it print?")



class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def update_user(self):
        while True:
            try:
                name = input("What is your name? \n")
                age = input("How old are you? \n")
                return self(name, age)
            except:
                print("wrong")
                continue



player = user.update_user()

print()

print(player.age)

print(f"Thank you {player.name}, we have added your age {player.age}")