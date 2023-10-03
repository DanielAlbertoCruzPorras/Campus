#Daniel Cruz
"""
Lanzar dado y saber cuantas veces cayó 5
"""
import random

cont5 = 0

for i in range(100):
    dado = random.randrange(1,7)
    if dado == 5:
        cont5 += 1
print(f"El 5 cayó {cont5:.0f} veces.")


