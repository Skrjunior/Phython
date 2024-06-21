#Program na online evidenciu dobiehajucich bezcov maratonu
def triedenie(b):
    for i in range(len(b)-1):
        minimum=i
        for j in range(i+1,len(b)):
            if b[minimum][2]>b[j][2]:
                minimum=j
        b[i],b[minimum]=b[minimum],b[i]
    return b 

def vypis(a,device):
    if device == 1:
        nazov=input('Zadajte nazov suboru ')
        f=open(nazov,'w')
    else:
        f=None
    print('{:20}{:>5}{:>7}'.format('Meno','Cislo','Cas'),file=f)
    print('='*40,file=f)
    for i in range(len(a)):
        if a[i][2]!=0.0:
            print('{:<20}{:>5}{:>7}'.format(a[i][1],a[i][0],a[i][2]),file=f)
    return 0

################ HLAVNY PROGRAM ##################
pole=[]
pole2=[]
while 1==1:
    cislo=int(input('Zadajte cislo '))
    if cislo == 0:
        break
    je=True
    for i in range(len(pole)):
        if pole[i][0] == cislo:
            je=False
            print('Pretekar ',cislo,' uz existuje v evidencii!' )
    if je:
        meno=input('Zadajte meno ')
        vektor=[]
        vektor.append(cislo)
        vektor.append(meno)
        vektor.append(0.0)
        pole.append(vektor)
        
print('Vkladajte cislo a cas:')
while True:
    ret=input()
    pp=ret.split()
    if int(pp[0]) == 0:
        print('Koniec programu.....')
        break
    else:
        cislo=int(pp[0])
        cas=float(pp[1])
        for i in range(len(pole)):
            if pole[i][0]==cislo:
                pole[i][2]=cas
    pole2=triedenie(pole)
    print()
    vypis(pole2,0)
