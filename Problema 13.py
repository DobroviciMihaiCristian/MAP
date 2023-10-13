x=int(input("Introduceti cate numere va avea lista:"))
y=[]
sum=0

for i in range(0,x,1):
    z=int(input("Introduceti numarul:"))
    y.append(z)

for i in range(0,x,1):
    sum=sum+y[i]

print("Suma numerelor din lista este:",sum)
print("Media aritmetica a numerelor din lista este:",int(sum/x))