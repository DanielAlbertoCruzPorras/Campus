import json

fd = open("D:\Mi GitHUB\Campus\lista.json", "w")
lst = []
for i in range(5):
    g = {"1":"pepe","2":20,"3":5}
    lst.append(g)
    json.dump(lst, fd)

fd.close()

fd = open("D:\Mi GitHUB\Campus\lista.json", "r")
lst = []
lst = json.load(fd)

for e in lst:
    print(f"Nick: {e['1']}")
    print(f"Tiempo: {e['2']}")
    print(f"Turnos: {e['3']}")

fd.close()