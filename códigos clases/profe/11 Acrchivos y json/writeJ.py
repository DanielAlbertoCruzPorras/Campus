import json

fd = open("/home/spukN01-011/Documents/Daniel Cruz/Campus/códigos clases/profe/11 Acrchivos y json/lista.json", "w")

lst = [{"Nombre":"Daniel","Edad":23},{"Nombre":"María","Edad":21},{"Nombre":"Diego","Edad":24}]

json.dump(lst, fd)

fd.close()

