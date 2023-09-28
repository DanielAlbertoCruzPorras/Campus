# Daniel Alberto Cruz Porras
valor_total = 0
c = 1
while c == 1:
    while True:
        N = int(input("Digite la cantidad de estudiantes: "))
        if N < 0:
            print("Cantidad de estudiantes inválida, intentelo de nuevo:")
            continue
        for i in range(N):
            while True:
                nombre = input("Digite el nombre del estudiante: ")
                if nombre.isalnum() == False:
                    print("Nombre inválido, intentelo de nuevo: ")
                    continue
                break

            while True:
                cod = input("Digite el código del estudiante: ")
                if cod.isdigit() == False or len(cod) != 6:
                    print("El código es inválido, recuerde que es un número entero de 6 dígitos, intentelo de nuevo: ")
                    continue
                break

            while True:
                try:
                    programa = int(input("Digite el progroma al que pertenece el estudiante: \n1:Técnico en Sistemas \n2:Técnico en Desarrollo de Videojuegos \n3:Técnico en Animación Digital \n"))
                    if programa < 1 or programa > 3:
                        print("Programa inválido, digite 1, 2 o 3: ")
                        continue
                    break
                except ValueError:
                    print("Error. Programa inválido")

            while True:
                try:
                    indicador_beca = int(input("Digite el indicador de beca del estudiante: \n1:Beca por rendimiento \n2:Beca Cultural \n3:Sin Beca \n"))
                    if indicador_beca < 1 or indicador_beca > 3:
                        print("Indicador inválido, digite 1, 2 o 3: ")
                        continue
                    break
                except ValueError:
                    print("Error. Indicador inválido")

            if programa == 1:
                if indicador_beca == 1:
                    valor_matricula = 800000*0.5
                elif indicador_beca == 2:
                    valor_matricula = 800000*0.6
                else:
                    valor_matricula = 800000
            elif programa == 2:
                if indicador_beca == 1:
                    valor_matricula = 1000000*0.5
                elif indicador_beca == 2:
                    valor_matricula = 1000000*0.6
                else:
                    valor_matricula = 1000000
            else:
                if indicador_beca == 1:
                    valor_matricula = 1200000*0.5
                elif indicador_beca == 2:
                    valor_matricula = 1200000*0.6
                else:
                    valor_matricula = 1200000

            print(f"Nombre: {nombre} \nValor matrícula: ${valor_matricula:,.2f}")
            valor_total += valor_matricula
        
        break
    print(f"El valor de todas las matrículas en este grupo es de: {valor_total:,.2f}")
while True:
    c = input("Desea continuar? \n1:Si \n2:no \n")
    if c < 1 or c > 2:
        print("Error. Intente de nuevo")
        continue
    break


