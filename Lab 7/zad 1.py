import numpy as np

lista = []
for i in range(7 , -1 ,-1):
    a = 2**i
    lista.append(2**i)
print(lista)
lista1 = [2**i for i in range(7 , -1 ,-1)]
wagi = np.array(lista1)

liczba_bin = np.random.randint(low=0 , high=2 , size=8)
print(liczba_bin)
tab = wagi * liczba_bin
print(tab.sum())