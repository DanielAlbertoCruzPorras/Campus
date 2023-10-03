#Daniel Cruz
n=int(input("Digite la cantidad de estudiantes: "))
if n%1 != 0:
    print("Sea serio hermano!!")
else:
    print("empiece a digitar las notas: ")
    p = 0
    cont = 0
    p1 = 0
    for i in range(n):
        p = float(input())
        p1 += p
        cont += 1
prom=p1/cont
print(f"El promedio fué de: {prom:.2f} \nLa cantidad de notas fueron: {cont:.0f}")
