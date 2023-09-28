while True:
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Error. Número entero no válido.")

while True:
    try:
        num2 = int(input("Ingrese un número: "))
        suma = num1 + num2
        print(f"La suma es: {suma}")
        break
    except Exception as e:
        print(f"Error al intentar sumar.\n {e}")


while True:
    try:
        cat = int(input("Ingrese una categoría (1 ,2 o 3)"))
        if cat < 1 or cat > 3:
            print("Categoría inválida. Ingrese 1, 2 o 3")
            continue
        break
    except ValueError:
        print("Error. Categoría inválida.")

