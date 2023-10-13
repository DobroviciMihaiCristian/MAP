x=int(input("Introduceti numarul:"))
p=0
for i in range(1,x+1,1):
    if(x%i==0):
        p=p+1

if(p==2):
    print("Numarul introdus este prim")
else:print("Numarul introdus nu este prim")
