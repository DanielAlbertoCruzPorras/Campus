a = {1:1,2:2,3:3,4:4,5:5,6:6}
c = 0
for k in a.keys():
    c += 1
    print(a[k])
    if c%2 == 0:
        b = input("Desea continuar? \nSi->S \nNo->N\n")
        if b == "N":
            break
