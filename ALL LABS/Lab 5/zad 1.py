zestaw_1 = []
a = int(input("podaj liczbe :"))
import random
zestaw_1 = [random.randint(1,10) for f in range(a)]
print(zestaw_1)
a = int(input("podaj liczbe :"))
zestaw_2 = [random.randint(5,15) for g in range(a)]
print(zestaw_2)
h = int(input("Liczba :"))
if h in zestaw_1 and zestaw_2:
    print('Liczba jest w dwoch listach')
elif h in zestaw_2:
    print('Licza z zestawu')
else:
    print('Nie ma takiej liczby w obu zestawach')
zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)