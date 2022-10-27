a = int(input("podaj pierwsza liczbe:"))
b = int(input("podaj druga liczbe :"))

if (a>b):
    a,b = b,a

while (a <= b):
        print(a, end=" ")
        a= a+1


