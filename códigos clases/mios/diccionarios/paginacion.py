

dic = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}
i = 0
for k in dic.keys():
    i += 1
    print(dic[k])
    if i%3 == 0:
        a = input("Desea continuar?")
        if a != "S":
            break
    
    


