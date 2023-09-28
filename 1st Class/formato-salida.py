#Daniel Cruz+
#Ejemplos de formatear salida

#Con format
sueldo = 560000
print("Sueldo: ${:,}".format(sueldo))
interes = 2500.1415
print("Intereses: ${:,.2f}".format(interes))

#f-string
print(f"Sueldo: ${sueldo:,} Intereses: ${interes:,}")