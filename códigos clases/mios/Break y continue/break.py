#Daniel Cruz
""" 
Break
Calcular si un número es primo
 """
N = int(input("Digite el numero a verificar: "))
i = 1
S = 0
if N < 2:
    print("No es primo")
else:
    while i <= N:
        # print(f"i = {i+1}")
        if N % i == 0:
            S += 1
        # print(S)
        i += 1
    if S == 2:
        print(f"El número {N:.0f} es primo.")
    elif S > 2:
        print(f"El número {N:.0f} no es primo.")

# CALCULAR SI UN NUMERO ES PRIMO, DIVISIBLE POR SI MISMO Y POR 1

num = int(input("ingrese un numero:"))

if num < 2:
    print("no es primo")
elif num == 2:
    print("es primo")
else:
    esprimo = True
    for i in range(2,num):
        if num % i == 0:
            esprimo = False
            break

if esprimo == True:
    print("es primo")
else:
    print("no es primo, lo divide",i)