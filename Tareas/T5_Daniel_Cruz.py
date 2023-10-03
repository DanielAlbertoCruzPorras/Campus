def menu():
    while True:
        try:
            print("=============+ MENU +================\n1. Calcular combinatoria\n2. Convertir texto a numero\n3. Calcular IVA de una factura\n4. Salir\n=====================================")
            opcion = int(input("Opción [1-4]? >>>  "))
            if opcion < 1 or opcion > 4:
                print("Opción no válida. Solo enteros de 1 a 4.")
                continue
            return opcion
        except ValueError:
            print("Opción no válida. Solo enteros de 1 a 4.")
            input("Presione cualquier tecla para continuar...")

def ingresar_numero(entero_positivo):
    while True:
        try:
            num = int(input(entero_positivo))
            if num < 0:
                print("Error. Número negativo")
                continue
            return num
        except ValueError:
            print("Error. Número inválido")

def factorial(num):
    if num == 1:
        factorial = 1
    elif num == 2:
        factorial = 2
    else:
        factorial = 2
        for i in range(3, num+1):
            factorial *= i
    return factorial

def combinatoria():
    while True:
        n = ingresar_numero("Number of items to choose from:  ")
        k = ingresar_numero("Number of items to be chosen:  ")
        if n >= k:
            combinatoria = (factorial(n)) / (factorial((n - k)) * factorial(k)) #La otra fórmula es incorrecta
            resultado = print(f"The result of C({n:.0f},{k:.0f}) = {combinatoria:,.0f}")
            return resultado
        else:
            print("n cannot be greater than k...")
            continue
            
    
def quitar_letras():
    cadena_nueva = ""
    cad = input("Digite la cadena:\n")
    cad = cad.strip()
    for i in cad:
        if i.isdigit():
            cadena_nueva = cadena_nueva + i
    return cadena_nueva

def IVA(precio_bruto, IVA):
    valor = (1 + IVA / 100) * precio_bruto
    return valor


## -----------------------------------------Main-----------------------------------------

while True:
    opcion = menu()
    if opcion == 1:
        comb = combinatoria()
        print(f"La cantidad de combinaciones posibles para esa combinatoria es de: {cadena_resultado:.0f}")
        input("Press any key to continue...")
    elif opcion == 2:
        cadena_resultado = quitar_letras()
        print(f"La nueva cadena es: {cadena_resultado}")
        input("Press any key to continue...")
    elif opcion == 3:
        while True:
            try:
                valorProduct = float(input("Ingrese valor del producto: "))
                if valorProduct <= 0:
                    print("Ingrese un número mayor a 0.")
                    continue
                break
            except ValueError:
                print("Valor inválido, intente de nuevo...")
        valor_IVA = ingresar_numero("Ingrese porcentaje del IVA: ")
        total = IVA(valorProduct , valor_IVA)
        print(f"El valor del producto aplicando un IVA del {valor_IVA}% es: ${total:,.2f} COP")
        input("Press any key to continue...")
    else:
        break