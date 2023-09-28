#Daniel Cruz
#Ejercicio 1

total_ventas = 0
comisiones_totales = 0
while True:
    cedula = int(input("Ingrese su numero de cedula: \nsi desea salir del programa digite (-1): \n"))
    if cedula == -1:
        break
    nombre = input("Ingrese su nombre: \n")
    tipo_vendedor = int(input("1. Puerta a puerta. \n2. Telemercadeo.  \n3. Ejecutivo en ventas. \nEscoja el tipo de vendedor: "))
    valor_ventas = int(input("Ingrese el valor las ventas realizadas en el mes: "))

    if tipo_vendedor == 1:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.2
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: ${comision:,.2f}\n")
    elif tipo_vendedor == 2:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.15
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: ${comision:,.2f}\n")
    elif tipo_vendedor == 3:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.25
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: ${comision:,.2f}\n")

print(f"El valor total de ventas es: ${total_ventas:,.2f} \ny el valor a pagar de comisiones es: ${comisiones_totales:,.2f}")


#Ejercicio 2
N = int(input("Digite la cantidad de conductores a liquidar: "))
C=0
cond_novatos = 0
cond_expertos = 0
valor_todos = 0
while C < N:
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    clase_conductor = int(input("Digite el tipo de conductor, 1 para experto y 2 para novato: "))
    valor_pasajes = float(input("Digite el valor toal por concepto de pasajes: "))
    valor_encomiendas = float(input("Digite el valor toal por concepto de encomiendas: "))
    if clase_conductor == 1:
        valor_total = valor_pasajes*0.3 + valor_encomiendas*0.2
        valor_todos += valor_total
        cond_expertos += 1
        print(f"El valor a pagarle al conductor {nombre} es de ${valor_total:,.2f}")
    elif clase_conductor == 2:
        valor_total = valor_pasajes*0.2 + valor_encomiendas*0.15
        valor_todos += valor_total
        cond_novatos += 1
        print(f"El valor a pagarle al conductor {nombre} es de ${valor_total:,.2f}")
    else:
        print("Clase de conductor inválida")
    C += 1
print(f"El valor a pagar a la totalidad de conductores es de {valor_todos:,.2f} \nLa cantidad de conductores novatos fue de: {cond_novatos} y la cantidad de conductores expertos fue de: {cond_expertos}")

#Ejercicio 3
N = int(input("¿Cuantos docentes son? "))
C = 0
pagar_general = 0
contA = 0
contB = 0
contC = 0
while C < N:
    documento = input("Ingrese el documento del docente: ")
    name = input("Ingrese el nombre del docente: ")
    contHoras = int(input("Ingrese la cantidad de horas laboradas: "))
    categoria = input("Ingrese la categoria del docente: A, B o C \nLa categoria del docente e :")

    if categoria == "A" or categoria =="a":
        salario = contHoras*25000
        contA += 1
        print(f"El salario de este docente es: ${salario:,.2f}")
    elif categoria == "B" or categoria == "b":
        salario = contHoras*35000
        contB += 1
        print(f"El salario de este docente es: ${salario:,.2f}")
    elif categoria == "C" or categoria == "c":
        salario = contHoras*50000
        contC += 1
        print(f"El salario de este docente es: ${salario:,.2f}")
    pagar_general += salario
    C += 1

print("="*18,"INFORME GENERAL","="*18)
print(f"Las ganacias de todos los docentes es: ${pagar_general:,.2f}")
print(f"Hay {contA} docentes categoria A,{contB} categoria B y {contC} categoria C")


