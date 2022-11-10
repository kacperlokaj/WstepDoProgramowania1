# Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
# • Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# • Oblicz średnią punktów liczbę punktów z egzaminu
# • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
# • Wyświetl punkty poniżej średniej
# • Wyświetl punkty powyżej średniej

import random
punkty = []
for i in range(15):
    a = random.uniform(0, 50)
    a = round(a,2)
    punkty.append(a)
print(punkty)
print("Wartosc maksymalna: ", max(punkty))
print("Wartosc minimalna: ", min(punkty))
b = float(input("Podaj liczbe punktow: "))
if b in punkty:
    c = punkty.index(b)
    print(c)
else:
    print("wartosc nie wystepuje w liscie ")
y=sum(punkty)
print("srednia", round(y/n,2))
sr = round(y/n,2)
punkty_2=[]
for i in range(n):
    if punkty[i] > sr:
        punkty_2.append(punkty[i])
print(punkty_2)


