fd = open("/home/spukN01-011/Documents/Daniel Cruz/Campus/códigos clases/profe/11 Acrchivos/mbox-short.txt","r")
fd2 = open("/home/spukN01-011/Documents/Daniel Cruz/Campus/códigos clases/profe/11 Acrchivos/enviados.txt","w")

lstEmails = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

for i in range(len(lstEmails)-1,-1,-1):
    msj = f"{lstEmails[i]} enviado [ok]"
    print(msj)
    fd2.write(msj+"\n")


fd.close()
fd2.close()

