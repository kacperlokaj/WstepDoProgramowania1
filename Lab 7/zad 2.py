
import numpy as np
tab2=np.random.randint(low=0,high=50,size=(5,5))
print(tab2)
print("maxium wartosc=",tab2.max())
print("minimum wartosc=",tab2.min())
print("maximum wartosc wiersza=",tab2.max(axis=1))
print("maximum wartosc kolumn=",tab2.max(axis=0))
print("maximum wartosc wiersza=",tab2.max(axis=1))
print("minimum wartosc kolumn=",tab2.max(axis=0))
print(tab2.sum(axis=1))
print(tab2.sum(axis=0))