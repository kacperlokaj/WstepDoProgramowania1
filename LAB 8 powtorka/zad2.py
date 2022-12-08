#Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
#dict1 = {'data1':10, 'data2':-4, 'data3':2}


def sum_of_values(slownik):
    suma = 0
    for v in slownik.values():
        suma = suma + v
    return suma

dict1 = {'data1':10, 'data2':-4, 'data3':2}
s = sum_of_values(dict1)
print(s)

