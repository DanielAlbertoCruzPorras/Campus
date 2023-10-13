import json

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar\n2. Modificar\n3. Borrar\n4. Ver\n5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargar_info(lstPersonal, ruta):
    try:
        fd = open(ruta,"r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return None
    fd.close()
    return lstPersonal

def leerID():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def leer_nombre():
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

def leer_edad():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leer_sexo():
    while True:
        try:
            sex = input("Ingrese el sexo del empleado: ")
            if len(sex) == "" or not sex.isalpha():
                print("Nombre inválido")
                continue
            return sex
        except Exception as e:
            print("Error al ingresar el sexo.", e)

def leer_tlf():
    while True:
        try:
            n = input("Ingrese el teléfono del empleado: ")
            if len(n)!=10 or not n.isnumeric():
                print("Teléfono inválido. Debe tener 10 decimales")
                continue
            return n
        except Exception as e:
            print("Error al ingresar el teléfono.\n", e)

def agregar(lstPersonal):
    print("\n\n*** 1. Agregar Personal\n")
    id = leerID()
    if existeid(id, lstPersonal):
        print("El id ya existe en la lista")
        input()
        return
    nombre = leer_nombre()
    edad = leer_edad()
    sexo = leer_sexo()
    telefono = leer_tlf()
    lstPersonal[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    guardar()

def guardar():
    try:
        fd = open(ruta,"w")
    except Exception as e:
        print("Error al intentar abrir el archivo\n", e)
        return None
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la información\n", e)
        return None
    fd.close()
    input("Empleado guerdado con exito.\nPresione cualquier tecla para continuar:")

def existeid(id, lstPersonal):
    for datos in lstPersonal:
        k = datos.kays()[0]
        if k == id:
            return True
    return False

# MAIN
ruta = ""
lstPersonal = []
cargar_info(lstPersonal, ruta)
while True:
    op = menu()
    if op == 1:
        agregar(ruta, lstPersonal)
        #agregar
        pass
    elif op == 2:
        #modificar
        pass
    elif op == 3:
        #borrar
        pass
    elif op == 4:
        #ver
        pass
    else:
        #salir
        print("\n Gracias por usar el programa.")
        break