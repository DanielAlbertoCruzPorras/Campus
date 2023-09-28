#Daniel Cruz
#N(usuarios de servicio del agua, se suministra por usuario) código, Nombre, Estado(v de vigente o s de suspendido), estrato(de 1 a 6) y consumo del mes en cm3  Se calcula el costo con valor de tarifa + valor consumo donde valor tarifa = (estrato - tarifa básica):(1 - $10000, 2 - $20000, 3 - $30000, 4 - 45000, 5 - 60000, 6 - 70000)   el valor del consumo es el consumo del mes * $200   Se debe imprimir nombre, valor de tarifa básica, valor de consumo y  valor a pagar por concepto de agua. Solo se liquida a los usuarios vigentes.
n=int(input("Digite la cantidad de usuarios: "))
consumo_total = 0
for i in range(1,n+1):
    print(f"Datos del usuario #{i}")
    cod = input("Código: ")
    nom = input("Nombre: ")
    est = input("Estado (V para vigente y S para suspendido): ")
    estr = input("Estrato: ")
    con = int(input("Consumo: "))
    if est == "V" or est == "v":
        if estr == 1:
            tar_bas = 10000
        elif estr == 2:
            tar_bas = 20000
        elif estr == 3:
            tar_bas = 30000
        elif estr == 4:
            tar_bas = 450000
        elif estr == 5:
            tar_bas = 60000
        elif estr == 6:
            tar_bas = 70000
        else:
            tar_bas = 0
        val_cons = con * 200
        val_a_pag = tar_bas + val_cons
        consumo_total += val_a_pag
        print("\n","=" * 40)
        print(f"\tNombre: {nom}")
        print(f"\tValor tarifa básica: {tar_bas}")
        print(f"\tValor consumo: {val_cons}")
        print(f"\tValor a pagar: {val_a_pag}")
# Imprimir el total a pagar por todos los usuarios
print()
print("\n")
print(f"El valor total a pagar es: {consumo_total:,.2f}")

