#Daniel Cruz
# tres enteros y mostrar de mayor a menor
""" v = [int(input("digite el primer número:")),int(input("digite el segundo número:")),int(input("digite el tercer número:"))]
v.sort(reverse=True)
print(v) """

n1 = int(input("incerte el primer número:"))
n2 = int(input("incerte el segundo número:"))
n3 = int(input("incerte el tercer número:"))

if n1>=n2 and n1>=n3:
    if n2>=n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2>=n1 and n2>=n3:
    if n1>=n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
elif n3>=n1 and n3>=n2:
    if n1>=n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)


