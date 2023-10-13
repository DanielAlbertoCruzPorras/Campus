import json
fd = open("/home/spukN01-011/Documents/Daniel Cruz/Campus/códigos clases/profe/11 Acrchivos y json/lista.json", "r")
lst = []
lst = json.load(fd)
for e in lst:
    print(f"Nombre: {e['Nombre']}")
    print(f"Edad: {e['Edad']}")
    print("-"*30)
fd.close()