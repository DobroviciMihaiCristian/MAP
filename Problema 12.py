x=int(input("Introduceti numarul:"))

a=0
b=1
f=0

while(f<x):
    print(f)
    f=a+b
    a=b
    b=f
