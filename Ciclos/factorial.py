#Daniel Cruz
n = int(input("Ingrese el numero al que desea calcularle el factorial: "))
n1 = n
r = 1
if n%1 != 0:
    print("Sea serio hermano!!")
else:
    for i in range(n):
        r *= i+1
print(f"El factorial de {n1:.0f} es {r:.2f}")