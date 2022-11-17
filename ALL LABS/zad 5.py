x=int(input("Liczba studentów:"))
y=1 #liczba z której zacznemy liczyć
suma=0
while (y<=x):
    print("Prosze napisać punkty studenta ",y, end=' ')
    b=int(input())
    y=y+1
    suma=suma+b
z=suma/x
print("średnia liczba punktów:",z)