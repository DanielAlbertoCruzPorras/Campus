#Daniel Cruz
# Ejercicio 1.0 (While)
#Verificar si un numero es perfecto o no
N = int(input("Digite el número a consultar: "))
S = 0
M = 0
i = 1
while i < (N-1):
    # print(f"i = {i+1}")
    if N % i == 0:
        S += i
        # print(S)
    i += 1


if S == N:
    print(f"El número {N:.0f} SI es un número perfecto.")
else:
    print(f"El número {N:.0f} NO es un número perfecto.")

# Ejercicio 1.1 (For)
#Verificar si un numero es perfecto o no
N = int(input("Digite el número a consultar: "))
S = 0
M = 0
for i in range(N-1):
    # print(f"i = {i+1}")
    if N % (i+1) == 0:
        S += (i+1)
        # print(S)

if S == N:
    print(f"El número {N:.0f} SI es un número perfecto.")
else:
    print(f"El número {N:.0f} NO es un número perfecto.")

# Ejercicio 2.0 (While)
#En cuantos años la matrícula dobla su valor, aumento de 7% anual (Compuesto)
P = 10000
B = 0
C = 0
while B == 0:
    C += 1
    P += 0.07*P
    if P >= 20000:
        B = 1
print(f"Se necesita que transcurran {C:.0f} años para que la matrícula valga el doble.") 

# Ejercicio 2.1 (For)
#En cuantos años la matrícula dobla su valor, aumento de 7% anual (Compuesto)
P = 10000
B = 0
C = 0
for i in range(100):
    if P < 20000:
        C += 1
        P += 0.07*P
print(f"Se necesita que transcurran {C:.0f} años para que la matrícula valga el doble.") 


#Ejercicio 3.0 (While)
#Aproximación a Pi 
import random
import math as ma

X = []
Y = []
H = []
B = 0
C = 0
while B < 1000000:
    X.append(random.uniform(0, 1))
    Y.append(random.uniform(0, 1))
    H.append(ma.sqrt((ma.pow(X[B],2)+ma.pow(Y[B],2))))
    if H[B] < 1:
        C += 1
    B += 1
Pi = 4*C/1000000
print(f"Bajo el experimento nuestra variable de aproccimación a Pi vale: {Pi:.6f} \nY nuestro -numberOfHits- fué de: {C:,}")

#Ejercicio 3.1 (For)
#Aproximación a Pi 
import random
import math as ma

X = 0
Y = 0
H = 0
C = 0
for i in range(10000000):
    X = random.uniform(0, 1)
    Y = random.uniform(0, 1)
    H = ma.sqrt((ma.pow(X,2)+ma.pow(Y,2)))
    if H <= 1:
        C += 1
Pi = 4*C/10000000
print(f"Bajo el experimento nuestra variable de aproccimación a Pi vale: {Pi:.6f} \nY nuestro -numberOfHits- fué de: {C:,}")



