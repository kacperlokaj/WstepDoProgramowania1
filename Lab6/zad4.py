def z4(**kwargs):
    if'end' in kwargs:
        pom=kwargs["end"]
    else:
        pom='\n'
    print(kwargs)
    for k in kwargs:
        print(k,' = ', kwargs[k],end=pom)

z4(dom=1,ulica="lwowska",kodpocztowy="35-202")

z4(dom=7,ulica="lwowska", kodpocztowy="35-202",end=' ')
