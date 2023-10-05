# Los conjuntos son listas sin elementos repetidos
# Las tuplas se crean con paréntesis () en vez de corchetes []

""" n = int(input("English newspaper: "))
setEng = set()
for i in range(n):
    setEng.add(input())

n = int(input("French newspaper: "))
setFrench = set()
for i in range(n):
    setFrench.add(input())
    
result = setEng - setFrench
print("Student only English newspapers:", len(result)) """


# Diccionarios se crean con llaves {}, consta de clave y valor, con el formato... {clave:valor,clave2:valor2,clave3:valor3...}

capitales = {"Colombia":"Bogotá","Brasil":"Rio de Janeiro","Francia":"París"}
print(capitales["Colombia"])
empleado = {"Nombre":"Sergio Medina","Cargo":"Programador","Salario":4000000}
print(empleado["Cargo"])
print(empleado.get("Apellido","Llave no existe"))
empleado["Sexo"] = "M"
empleado["Salario"] = 5000000
print(empleado)
del empleado["Sexo"]
print(empleado)

# Borrar todo el diccionario
""" empleado = {}
empleado.clear()
del empleado """

oficina = empleado
print(oficina)
oficina["Salario"] = 6000000
print(oficina)
print(empleado)

oficina = empleado.copy()
print(oficina)
oficina["Salario"] = 5000000
print(oficina)
print(empleado)



