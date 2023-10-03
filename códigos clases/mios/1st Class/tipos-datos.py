#Daniel Cruz
edad = 25 #tipo entero
print(type(edad))
edad = "daniel" #tipo cadena
print(type(edad))
#tipo float
temp = 33.5
print("temp:",type(temp))
#tipo lógico
soltero = True #false
print("soltero:",type(soltero))
prueba = "3.1415"
if prueba: #No importa el tipo de la variable 
           #siempre que tenga algo dentro
    print("Si sirve, pero la variable prueba es de tipo...", type(prueba))
else:
    print("No es así")
