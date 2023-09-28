#Ejercicio 1
"""
num = input("Ingrese el número: ")
if num.startswith("+") and num.count("-") == 2:
    partes = num.split("-")
    print(f"El número es: {partes[1]}")
else:
    print("Error. El número no cumple con el formato.")

#Ejercicio 2
palabra = input("Ingrese una palabra para ver si es palíndrome: ")
palabra2 = palabra[::-1]
print(f"{palabra2[1]}")
palabra = palabra.capitalize()
palabra2 = palabra2.capitalize()
if palabra == palabra2:
    print("Es palíndrome")
else:
    print("No es palíndrome")

#Ejercicio 3

fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa : ")
partes = fecha_nacimiento.split("/")
e = 0
for e in range(3):
    if partes[e].isdecimal() == True and int(partes[2])>1000:
        dia = partes[0]
        mes = partes[1]
        año = partes[2]
    else:
        e = 3
if e == 0:
    print(f"Dia: {dia}\nMes: {mes}\nAño: {año}\n")
else:
    print("Hay un error en la fecha")
"""

#Ejercicio 4
cadena = input("Introduzca una cadena: ")
if cadena.isascii() == True:
    while True:
        lon1 = len(cadena)
        for i in range(len(cadena)):
            if len(cadena) > 2:
                if cadena[i] == cadena[i+1]:
                    cadena = cadena[0:i,i+2:len(cadena)]
                lon2 = len(cadena)
        if lon1 == lon2:
            break




