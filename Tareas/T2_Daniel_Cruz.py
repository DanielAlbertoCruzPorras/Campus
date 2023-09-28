#Daniel Cruz
#Ejercicio 1
distancia = int(input("Digite la distancia del viaje en kilómetros: "))
dias = int(input("Digite la cantidad de días de la estancia: "))
precio_bruto = distancia*0.63
if distancia > 800 and dias > 7:
    precio = 2*(precio_bruto*0.7)
else:
    precio = 2*precio_bruto
print(f"El costo de los ticketes de ida y regreso sería de: $ {precio:,.2f}")

#Ejercicio 2
año = int(input("Digite el año a consultar: "))
c1 = año%4
c2 = año%100
c3 = año%400
if c1==0:
    if c2==0: 
        if c3 == 0:
            b = "es bisiesto"
        else:
            b = "no es bisiesto"
    else:
        b = "es bisiesto"
else:
    b= "no es bisiesto"
print("El año que a consultado ",b)

#Ejercicio 3
"""
Se calcula dividiendo el peso en kg 
entre el cuadrado de la altura en 
metros, obteniendo:
Calculo<18.5 bajo de peso
18.5<=calculo<25 normal
25.0<=calculo<30 sobrepeso
calculo>30 obesidad

pida el peso en libras y la 
altura en pulgadas y luego
muestre el BIM (calculo)
1 lb = 0.45359237 kg
1 in = 0.0254 m
"""
w = int(input("Enter weight in pounds: "))
h = int(input("Enter height in pounds: "))
h1 = h*0.0254
w1 = w*0.45359237
bim = w1/(h1*h1)
if bim<18.5:
    print(f"Underweight and BMI: {bim}")
elif 18.5 <= bim and bim < 25:
    print(f"Normal and BMI: {bim}")
elif 25 <= bim and bim < 30:
    print(f"Overweight and BMI: {bim}")
else:
    print(f"Obese and BMI: {bim:.2f}")

#Ejercicio 4
"""
pedir que el usuario ingrese un número de
0 a 6 donde 0 es a domingo como 1 a lunes
y 6 a sábado, luego pidale que digite el numero de días transcurridos desde hoy hasta un día futuro, luego imprima el día futuro
"""
hoy = int(input("Enter today is day: "))
futuro = int(input("Enter the number of days elapsed since today:"))
v= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
a = futuro//7
n = futuro - a*7
f = hoy + n
if f>6:
    f=f-7
print(f"Today is {v[hoy]} and the future day is {v[f]}")

# Ejercicio 5
num=int(input("Incerte el entero positivo: "))
if num<0:
    num= int(input("Por favor incerte un valor válido: "))
    if num<0:
        print("Sea serio mano!!")
elif num//10 == 0:
    print("Este número tiene 1 decimal")
elif num//100 == 0:
    print("Este número tiene 2 decimales")
elif num//1000 == 0:
    print("Este número tiene 3 decimales")
elif num//10000 == 0:
    print("Este número tiene 4 decimales")
elif num//100000 == 0:
    print("Este número tiene 5 decimales")
elif num//1000000 == 0:
    print("Este número tiene 6 decimales")
elif num//10000000 == 0:
    print("Este número tiene 7 decimales")
elif num//100000000 == 0:
    print("Este número tiene 8 decimales")
elif num//1000000000 == 0:
    print("Este número tiene 9 decimales")
elif num//10000000000 == 0:
    print("Este número tiene 10 decimales")
elif num//100000000000 == 0:
    print("Este número tiene 11 decimales")
elif num//1000000000000 == 0:
    print("Este número tiene 12 decimales")
elif num//10000000000000 == 0:
    print("Este número tiene 13 decimales")
elif num//100000000000000 == 0:
    print("Este número tiene 14 decimales")
elif num//1000000000000000 == 0:
    print("Este número tiene 15 decimales")
elif num//10000000000000000 == 0:
    print("Este número tiene 16 decimales")
elif num//100000000000000000 == 0:
    print("Este número tiene 17 decimales")
elif num//1000000000000000000 == 0:
    print("Este número tiene 18 decimales")
elif num//10000000000000000000 == 0:
    print("Este número tiene 19 decimales")
elif num//10000000000000000000 == 0:
    print("Este número tiene 19 decimales")

