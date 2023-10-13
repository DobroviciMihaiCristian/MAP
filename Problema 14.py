x=int(input("Introduceti cate numere va avea lista:"))
y=[]

for i in range(0,x,1):
    z=int(input("Introduceti numarul:"))
    y.append(z)

y.sort

print("Cel mai mic numar din lista este:",y[0])
print("Cel mai mare numar din lista este:",y[x-1])