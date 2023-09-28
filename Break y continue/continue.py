#Daniel Cruz
"""
Continue
Escibir los números de 1 a 100 excepto los multiplos de 7
"""
for i in range(1,101):
    if i % 7 == 0:
        continue
    print(i, end=", ")