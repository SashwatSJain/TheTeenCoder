# VIRTUAL DICE
import random
while True:
    x = str(input('press enter to roll a dice, anything else to quit'))
    if x !="":
        break
    else:
        print(random.randint(1, 6))