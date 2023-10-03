s = "Yo soy tu PADRE!!"

#Recorrido por indice
for i in range(len(s)):
    print(s[i], end=",")
print("\n")
#recorrido por elemento
for e in s:
    print(e, end=",")
print("\n")
#slice, imprimir desde una posición dada o un rango de la cadena
print(s[2:])
print(s[4:7]) #imprime s[4], s[5] y s[6]

#invertir cadena
print(s[::-1])

#operador in
print("tu" in s)
print("tu" not in s)

#funciones
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("o"))
print(s.find("o"))
print(s.center(40))
print(s.rfind("o"))

c = "100"
print(c.isdigit())
print(c.isalpha())
print(c.isalnum())
print(c.isdecimal())
print(c.isspace())
print(c.startswith("1"))
print(c.endswith("1"))
b = "Daniel Cruz"
a = b.split()
print(b.split())
print(b.split("C"))
print(a)


c = "100a"
print(c.isdigit())
print(c.isalpha())
print(c.isalnum())
print(c.isdecimal())
print(c.startswith("0"))
print(c.endswith("a"))


