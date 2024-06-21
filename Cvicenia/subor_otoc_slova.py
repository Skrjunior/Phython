#PROGRAM ktory otaca slova vo vetach suboru
def slova_otoc(ret):
    veta=''
    while len(ret)>0 and ret.find(' ')>0:
        pozicia=ret.find(' ')
        slovo=''
        for i in range(len(ret[:pozicia]),-1,-1):
            slovo=slovo+ret[i]
        veta=veta+slovo+' '
        ret=ret[pozicia+1:]
    if len(ret)>0:
        for i in range(len(ret)-1,-1,-1):
            veta=veta+ret[i]
    return veta

#main program #################
nazov=input('Zadajte nazov suboru ')
f=open(nazov,'r')
nazov2=input('Zadajte subor na zapis: ')
f2=open(nazov2,'w')
for riadok in f:
    riadok=riadok.replace('\n','')
    riadok=slova_otoc(riadok)
    print(riadok)
    print(riadok,file=f2)
f.close()
f2.close()
