import math

a=int(input("Introduceti valoarea pentru a:"))
b=int(input("Introduceti valoarea pentru b:"))
c=int(input("Introduceti valoarea pentru c:"))

print("Ecuatia introdusa este:",a,"X^2+",b,"X+",c)

delta=b*b-4*a*c
if delta>0:
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print("Solutiile ecuatiei sunt:",x1,"si",x2)
elif delta==0:
    print("Solutiile ecuatiei sunt egale intre ele, x1=x2=:",-b/2*a)
else:print("Ecuatia nu are radacini reale")
