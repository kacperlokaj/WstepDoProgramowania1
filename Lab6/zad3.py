def z3(*krotka):
    print(krotka)
    for x in krotka:
        print(x)

z3(1,2,3,4,5.45 , 7.21)

z3()

z3("dom" , [1,2,3])

def maximum (*args):
    pom=args[0]
    for a in args[1:]:
        if pom < a:
            pom =a
    return pom

maks = maximum(1,2,10,2,6)
print(maks)

maks = maximum()
print(maks)