r = 1
while r == 1:
    cadena = input("Digite la cadena a reducir: ")
    lon = len(cadena)
    i = 0

    if cadena.isalpha() and cadena.islower():
        while True:
            
            lon1 = len(cadena)
            for i in range(len(cadena)):
                if i < (len(cadena)-1):
                    if cadena[i] == cadena[i+1]:
                        cadena = cadena[0:i] + cadena[i+2:len(cadena)+1]
                    lon2 = len(cadena)
                    lon = len(cadena)
                    i += 1
                    print(f"cadena: {cadena}\nlongitud1: {lon1}  longitud2: {lon2}")
                if lon1 != lon2:
                    i = lon1
            lon2 = len(cadena)
            print(f"cadena: {cadena}\nlongitud1: {lon1}  longitud2: {lon2}")
            if lon1 == lon2:
                break
        if cadena == "":
            print(f"Empty string")
        print(f"{cadena}")
    r = int(input("Desea seguir con otra cadena (si=1 ; no=0)?:"))