import numpy as np
import os
import sys

rng = np.random.default_rng()

sample_1 = rng.integers(10, size=6)
sample_2 = rng.integers(10, size=6)
sample_3 = rng.integers(10, size=4)


print(sample_1, sample_2, sample_3)

print(sample_3[2:])

print((str(sample_3[0])) + (str(sample_3[1])))



wires = ["blue", "red", "yellow"]
print(wires)

correct_wire = np.random.choice(wires, replace = False)

print(correct_wire)

cuts = 0
while cuts < 3:
    user_wire = input("What color wire will you cut:  ")
    if user_wire == correct_wire:
        print("whew!")
    else:
        cuts += 1
        print("Beep......beep.....beep....")
        print("\"nothing happened\"")
if cuts == 3:
    sys.exit()


