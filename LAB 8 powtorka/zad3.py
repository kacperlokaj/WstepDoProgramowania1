def potega(w,p):
    wyniki = []
    if len(w) != len(p):
        print("listy nie sa tej samej dlg")
        return wyniki
    for x in range (len(w)):
        wynik = w[x] ** p[x]
        wyniki.append(wynik)
    x=+1
    return wyniki


wartosci = [2,3,4,5]
potegi = [2,3,4,5]

rezultat = potega(wartosci,potegi)

print(rezultat)