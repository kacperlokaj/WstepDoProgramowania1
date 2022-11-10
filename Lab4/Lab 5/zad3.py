a=[]
b = int(input("podaj liczbe zwierząt:"))
for i in range(b):
    g=input("Podaj nazwe zwierzat:")
    a.append(g)
print(a)
a.sort()
print(a)
print(a[0],a[-3:],len(a))