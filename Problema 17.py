a=float(input("Introduceti valoarea primului unghi:"))
while a<0 or a>180:
    a=float(input("Introduceti alta valoare pentru primului unghi:"))

b=float(input("Introduceti valoarea pentru al doilea unghi:"))
while b<0 or b>180:
    b=float(input("Introduceti alta valoare pentru al doilea unghi:"))

c=float(input("Introduceti valoarea pentru al treilea unghi:"))
while c<=0 or c>=180:
    c=float(input("Introduceti alta valoare pentru al treilea unghi:"))

if a+b+c==180:
    print("Numerele introuduse pot reprezenta unghiurile unui triunghi:")
else:print("Numerele introuduse nu pot reprezenta unghiurile unui triunghi:")

