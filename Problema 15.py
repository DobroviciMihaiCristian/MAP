x=[]
aux=0
for i in range(0,8,1):
    z=int(input("Introduceti numarul de pe pozitia"))
    x.append(z)

print(x)
for i in range(0,8,1):
    for j in range(i+1,8,1):
        if(x[j]<x[i]):
            aux=x[j]
            x[j]=x[i]
            x[i]=aux


print(x)