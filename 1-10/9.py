# 9
# 6 April 2021
# Random string generator(it can also be used as a random password generator)

import random as r

a = int(input(">>"))

def rand():
    x = r.randint(63,122)
    return chr(x)

for x in range(a):
    print(rand(), end = "")
