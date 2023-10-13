x=int(input("Introduceti prima valoare:"))
y=int(input("Introduceti a doua valoare:"))
k=0

if x>y:
    for i in range(1,x+1,1):
        if x%i==0 and y%i==0:
            k=i

if y>x:
    for i in range(1,y+1,1):
        if x%i==0 and y%i==0:
            k=i
else: k=x
print("CMMDC al celor doua numere este:",k)
