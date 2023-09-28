#Daniel Cruz
# Ejercicio 1
cant_ast = int(input("Digite la cantidad de asteriscos deseados para la ultima fila: "))

for i in range(cant_ast):
    if i!=2:
        print("*"*(i+1))

# Ejercicio 2
alt = int(input("Digite la altura del rectángulo: "))
for i in range(alt):
    if i==0:
        print("*******")
    elif i==(alt-1):
        print("*******")
    else:
        print("*     *")

# Ejercicio 3
"""
calcular sueldo bruto y neto
sueldo bruto a partir de valor hora y horas trabajadas 
descuentos: valor de la eps que es el 4% y 
la pensión que es el 4%
El sueldo neto es el bruto menos descuentos
valor de la hora a 20K
"""
val_hora = 20000
horas_trabajadas = float(input("Digite las horas trabajadas: "))
print(f"Sueldo bruto: {(val_hora*horas_trabajadas):,.2f}  Descuento por EPS: {((val_hora*horas_trabajadas)*0.04):,.2f}  Descuento por Pensión: {((val_hora*horas_trabajadas)*0.04):,.2f} Sueldo neto: {((val_hora*horas_trabajadas)-2*((val_hora*horas_trabajadas)*0.04)):,.2f}")

# Ejercicio 4
seg = int(input("Digite los segundos: "))
hora = seg//3600
min = (seg-hora*3600)//60
seg_fin = seg - hora*3600 - min*60
print(f"{hora} Horas \n{min}  minutos \n{seg_fin} Segundos")

# Ejercicio 5

nota = float(input("Digite la nota en el rando de 0.0 a 5.0:"))
print(f"La curva de 8 para esa nota es: {(nota*0.8+1):.2f}")
