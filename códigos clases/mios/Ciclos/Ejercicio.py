#Daniel Cruz
#secuencia +-+-+-
# 1,1,2,-1,1,-2,?
a=1
b=1
c=-1
for i in range(5):
    d=a+(c**i)*b
    a=b
    b=d
    print(d, end=", ")

