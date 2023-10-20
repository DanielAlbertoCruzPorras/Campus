import time
import json

def menu():
    while True:
        try:
            print("==================\n TIC TAC TOE\n==================")
            print("1. Jugar\n2. Tabla de calificaciones\n3. Salir\n")
            op = int(input(">> Opción [1-3]?\n"))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione enter para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione enter para continuar...")

def pedir_nombre(a):
    while True:
        try:
            nom = input(a)
            if len(nom.strip()) == 0:
                print("Debe ingresar un nombre, intente de nuevo")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def dibujar_tablero(pos,casilla,c):
    if c%2 == 0:
        pos[casilla-1] = "O"
    else:
        pos[casilla-1] = "X"
    if c == 1.5:
        pos[0] = 1
    for i in range(13):
        if i==0 or i==4 or i==8 or i==12:
            print("+-------+-------+-------+")
        elif i>0 and i<4:
            if i==2:
                print(f"|   {pos[0]}   |   {pos[1]}   |   {pos[2]}   |")
            else:
                print("|       |       |       |")
        elif i>4 and i<8:
            if i==6:
                print(f"|   {pos[3]}   |   {pos[4]}   |   {pos[5]}   |")
            else:
                print(f"|       |       |       |")
        elif i>8 and i<12:
            if i==10:
                print(f"|   {pos[6]}   |   {pos[7]}   |   {pos[8]}   |")
            else:
                print(f"|       |       |       |")
        else:
            print("*     *")
    return pos

def ficha(datos1, datos2):
    while True:
        try:
            X = int(input("Decida que jugador usará el símbolo X y jugará primero; Escoja 1 ó 2\n"))
            if X != 1 and X != 2:
                print(f"Selección errónea, intente de nuevo.")
                continue
            elif X == 1:
                input(f"Iniciará el jugador {datos1[0]}, presione enter para iniciar.")
            elif X == 2:
                input(f"Iniciará el jugador {datos2[0]}, presione enter para iniciar.")
            return X
        except ValueError:
            print("Error al escoger, intente de nuevo")
            continue

def pedir_casilla(pos):
    while True:
        try:
            cas = int(input("Escoja la casilla donde desea jugar (número entre 1 y 9):\n"))
            if cas < 1 and cas > 9:
                print("Eror al seleccionar, intente de nuevo.")
                continue
            if pos[cas-1] == "X" or pos[cas-1] == "O":
                print("La casilla ya está tomada, seleccione otra.")
                continue
            return cas
        except ValueError:
            print("Error al escoger, intente de nuevo")
            continue

def juego(pos):
    turno = True
    datos1 = []
    datos2 = []
    c = 1
    datos1.append(pedir_nombre("Ingrese el nombre o apodo del jugador 1\n"))
    datos2.append(pedir_nombre("Ingrese el nombre o apodo del jugador 2\n"))
    X = ficha(datos1, datos2)
    tiempo_jugador1 = 0
    tiempo_jugador2 = 0
    casilla = 1
    while turno:
        tiempo_inicial = time.time()
        if c%2 != 0 and X == 2:
            input(f"Turno del jugador {datos2[0]}, presione enter para continuar")
        elif c%2 == 0 and X == 2:
            input(f"Turno del jugador {datos1[0]}, presione enter para continuar")
        elif c%2 != 0 and X == 1:
            input(f"Turno del jugador {datos1[0]}, presione enter para continuar")
        elif c%2 == 0 and X == 1:
            input(f"Turno del jugador {datos2[0]}, presione enter para continuar")
        if c == 1:
            c = 1.5
            pos = dibujar_tablero(pos,casilla,c)
            c = 1
        casilla = pedir_casilla(pos)
        pos = dibujar_tablero(pos,casilla,c)
        tiempo_final = time.time()
        tiempo_turno = tiempo_final - tiempo_inicial
        if c%2 != 0 and X == 2:
            tiempo_jugador2 += tiempo_turno
        elif c%2 == 0 and X == 2:
            tiempo_jugador1 += tiempo_turno
        elif c%2 != 0 and X == 1:
            tiempo_jugador1 += tiempo_turno
        elif c%2 == 0 and X == 1:
            tiempo_jugador2 += tiempo_turno
#0 | 1 | 2
#3 | 4 | 5
#6 | 7 | 8
        if c >= 5: #Verificar si hay ganador
            if pos[0] == pos[3] and pos[0] == pos[6]:
                if pos[0] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[1] == pos[4] and pos[1] == pos[7]:
                if pos[1] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[2] == pos[5] and pos[2] == pos[8]:
                if pos[2] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[0] == pos[1] and pos[0] == pos[2]:
                if pos[0] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[3] == pos[4] and pos[3] == pos[5]:
                if pos[3] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[6] == pos[7] and pos[6] == pos[8]:
                if pos[6] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[0] == pos[4] and pos[0] == pos[8]:
                if pos[0] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if pos[2] == pos[4] and pos[2] == pos[6]:
                if pos[2] == "X":
                    if X == 1:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
                    else:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                else:
                    if X == 1:
                        datos2.append(tiempo_jugador2)
                        turnos = c/2
                        datos2.append(turnos)
                        print(f"El ganador es: {datos2[0]} \nFelicitaciones!!")
                        return datos2
                    else:
                        datos1.append(tiempo_jugador1)
                        turnos = ((c-1)/2)+1
                        datos1.append(turnos)
                        print(f"El ganador es: {datos1[0]} \nFelicitaciones!!")
                        return datos1
            if c == 9:
                print(f"Es un empate, buen juego!!\n")
        c += 1

def set_pos():
    pos = [] #posición en que el jugador va a jugar
    for i in range(9):
        pos.append(i+1)
    return pos

def cargar_info(vect_juego, ruta):
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
            vect_juego = json.load(fd)
        else:
            vect_juego = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return None
    fd.close()
    return vect_juego

def guardar(ganador):
    try:
        fd = open("D:\Mi GitHUB\Campus\códigos clases\mios\Proyecto 1\ganadores.json","w")
    except Exception as e:
        print("Error.\n", e)
        return None
    try:
        json.dump(ganador, fd)
    except Exception as e:
        print("Error.\n", e)
        return None
    fd.close()
    input("Presione cualquier tecla para continuar:")

def leer_archivo(vect_juego,ruta):
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
            vect_juego = json.load(fd)
        else:
            vect_juego = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return None
    vec_aux = []
    for i in range(len(vect_juego)):
        vec_aux.append(vect_juego[i]['3'])
    vec_aux2 = []
    for i in range(len(vect_juego)):
        vec_aux2.append(vect_juego[i]['2'])
    for e in range(len(vec_aux)):
        m = e
        for i in range(len(vec_aux)):   # | 0 | 1 | 2 |
            if vec_aux[m] > vec_aux[i]:
                m = i
            if vec_aux[m] == vec_aux[i]:
                if vec_aux2[m] > vec_aux2[i]:
                    m = i
        print(f"Nombre: {vect_juego[m]['1']}")
        print(f"Tiempo: {vect_juego[m]['2']:.2f}")
        print(f"Turnos: {vect_juego[m]['3']:.0f}")
        print("-"*16)
        vec_aux[m] += 20
    fd.close()
    return

#Esta de abajo es matriz_juego

# #Nombre#Tiempo#Movimientos
# #Nombre#Tiempo#Movimientos
# #Nombre#Tiempo#Movimientos
# #Nombre#Tiempo#Movimientos

## MAIN
#crear un vector de 9 posiciones para saber si poner número o simbolo
vect_juego = []
ruta = "D:\Mi GitHUB\Campus\códigos clases\mios\Proyecto 1\ganadores.json"
cargar_info(vect_juego,ruta)
while True:
    op = menu()
    if op == 1:
        pos = set_pos()
        ganador = juego(pos)
        print(f"La cantidad de turnos usados fueron: {ganador[2]:.0f}\nEl tiempo fue de: {ganador[1]:.2f} seg\n")
        vect_juego = cargar_info(vect_juego,ruta)
        vect_juego.append({"1":ganador[0],"2":ganador[1],"3":ganador[2]})
        guardar(vect_juego)
        #print(vect_juego)
    elif op == 2:
        leer_archivo(vect_juego,ruta)
    else:
        print("\nGracias por Jugar; Hasta pronto.")
        break