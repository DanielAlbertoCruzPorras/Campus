#Daniel Cruz
c = 1
i = "S"
while i == "S":
    print(f"Datos del usuario #{c}")
    c += 1
    nom = input("Nombre: ")
    estr = int(input("Estrato: "))
    if estr == 1:
        tar_bas = 10000
    elif estr == 2:
        tar_bas = 15000
    elif estr == 3:
        tar_bas = 30000
    elif estr == 4:
        tar_bas = 50000
    elif estr == 5:
        tar_bas = 65000
    else:
        tar_bas = 0
    print("\n","=" * 30)
    print(f"\tNombre: {nom}")
    print(f"\tValor tarifa básica: {tar_bas}")
    i = int(input(f"Si desea continuar digite la letra S, si desea salir digite la letra N: "))
# Imprimir el total a pagar por todos los usuarios


