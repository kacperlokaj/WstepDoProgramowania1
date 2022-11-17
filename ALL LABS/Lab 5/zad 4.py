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
liczba_stud = 15
for i in range(liczba_stud):
    # punkty = random.random() * 100 % 50
    p = random.uniform(0, 50)
    punkty.append(round(p, 2))
print()
print(punkty)
print(f'min = {min(punkty)}')
print(f'max = {max(punkty)}')
p = float(input('Podaj liczbę punktów: '))
if p in punkty:
    print(punkty.index(p))
else:
    print(f'liczba {p} punktów nie występuje na liście')
print()

#Oblicz srednia liczbe punktów z egzaminu
y=sum(punkty)
sr = round(y/liczba_stud,2)
print("srednia",sr)
punkty_w =[]
for i in range (liczba_stud):
    if punkty[i] > sr:
        punkty_w.append(punkty[i])
punkty_n = [p for p in punkty if p < sr]
print(punkty_n, punkty_w, len(punkty_n), len(punkty_w))

