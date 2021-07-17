f=open("resultados.txt","r")
x=f.read()
x=x.split("\n\n")
path="./samplesC/"
tp=0
fn=0
fp=0
for i in range(len(x)-1):
    a=x[i].split("\n")
    print(a[0])
    g=open(path+a[0],"r")
    y=g.read()
    y=y.split(" ")
    perros=0
    gatos=0
    perrosd=0
    gatosd=0
    print(y)
    for j in range(len(y)):
        if("." not in y[j]):
            print(y[j])
            if y[j]=="0":
                perros+=1
            if y[j]=="1":
                gatos+=1
    perrosd=x[i].count("dog")
    gatosd=x[i].count("cat")
    
    print("gatos: "+str(gatos))
    print("perros: "+str(perros))
    print(str(gatosd))
    print(str(perrosd))
    
    if perrosd>perros:
        fp=fp+(perrosd-perros)
        tp=tp+perros
    if perrosd==perros:
        tp=tp+perros
    if perrosd<perros:
        tp=tp+perrosd
        fn=fn+(perros-perrosd)
        
    if gatosd>gatos:
        fp=fp+(gatosd-gatos)
        tp=tp+gatos
    if gatosd==gatos:
        tp=tp+gatos
    if gatosd<gatos:
        tp=tp+gatosd
        fn=fn+(gatos-gatosd)
        '''
    print("gatos/gatosd: "+str(gatos)+str(gatosd))
    print("perros/perrosd: "+str(perros)+str(perrosd))'''
print(str(tp))
print(str(fp))
print(str(fn))
z=open("tabla.txt","w")
z.write("True positive: "+str(tp)+"\n")
z.write("False positive: "+str(fp)+"\n")
z.write("False negative: "+str(fn)+"\n")
z.close()
f.close()