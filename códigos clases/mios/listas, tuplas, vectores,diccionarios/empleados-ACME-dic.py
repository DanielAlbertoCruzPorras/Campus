def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
""" def buscarEmpleado(dicEmpleados, idEmpl):
    # return dicEmpleados.get(idEmpl) != None
    return idEmpl in dicEmpleados """

def buscarEmpleado(dicEmpleados):
    print("\n\n3. Buscar Empleado\n")
    idEmpl = leerIDEmpl()
    if idEmpl in dicEmpleados == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", dicEmpleados[idEmpl]["nombre"])
    print("Horas trabajadas:", dicEmpleados[idEmpl]["HorasTrabajadas"])
    print("Valor de la hora:", dicEmpleados[idEmpl]["ValorHora"])
    print(f"Salario: ${dicEmpleados[idEmpl]['Salario']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")

def modificarEmpleado(dicEmpleados):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    if idEmpl in dicEmpleados == False:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        dicEmpleados[idEmpl]["nombre"] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        dicEmpleados[idEmpl]["HorasTrabajadas"] = cantHoras
        
    elif op == 3:
        valHora = leerValHoraEmpl()
        dicEmpleados[idEmpl]["ValorHora"] = valHora
        
    dicEmpleados[idEmpl]["Salario"] = dicEmpleados[idEmpl]["ValorHora"] * dicEmpleados[idEmpl]["HorasTrabajadas"]

def agregarEmpleado(dicEmpleados):
    print("\n\n*** 1. Agregar empleado\n")
    dicDatos = {}
    id = leerIDEmpl()
    if id in dicEmpleados:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreEmpl()
    dicDatos["HorasTrabajadas"] = leerHoraTrabEmpl()
    dicDatos["ValorHora"] = leerValHoraEmpl()
    dicDatos["Salario"] = dicDatos["ValorHora"] * dicDatos["HorasTrabajadas"]
    
    dicEmpleados[id] = dicDatos

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado\n2. Modificar empleado\n3. Buscar emplado\n4. Eliminar empleado\n5. Listar empleados\n6. Listar nómina de un empleado\n7. Listar nómina de todos los empleados\n8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

def eliminar_empleado(dicEmpleados):
    print("\n\n4. Eliminar Empleado\n")
    idEmpl = leerIDEmpl()
    if idEmpl in dicEmpleados == False:
        print("El código del empleado no existe.")
        input()
        return
    del dicEmpleados[idEmpl]
    print("Empleado eliminado exitosamente")

def listar_empleados(dicEmpleados):
    c = 0
    for k in dicEmpleados.keys():
        c += 1
        print(dicEmpleados[k])
        if c%5 == 0:
            b = input("Desea continuar? \nSi->S \nNo->N\n")
            if b == "N":
                return

def listar_nomina(dicEmpleados):
    print("\n\n6. Listar Nomina\n")
    idEmpl = leerIDEmpl()
    if idEmpl in dicEmpleados == False:
        print("El código del empleado no existe.")
        input()
        return
    valHora = dicEmpleados[idEmpl]["ValorHora"]
    cantHoras = dicEmpleados[idEmpl]["HorasTrabajadas"]
    minimo = 8510 #por hora
    
    

## PROGRAMA PRINCIPAL
dicEmpleados = {}
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()
    elif op == 2:
        modificarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()
    elif op == 3:
        buscarEmpleado(dicEmpleados)
    elif op == 4:
        eliminar_empleado(dicEmpleados)
    elif op == 5:
        listar_empleados(dicEmpleados)
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break