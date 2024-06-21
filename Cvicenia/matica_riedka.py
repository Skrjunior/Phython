#Program na riedke matice + a -
def nacitat():
    rmat={}            
    print('Zadajte prvky riedkej matice [riadok,stlpec,hodnota]')
    while 1==1:
        ret=input()
        if len(ret)==0 and ret=='':
            break
        temp=ret.split(' ')
        kluc=int(temp[0]),int(temp[1])
        hodnota=int(temp[2])
        rmat[kluc]=hodnota
    return rmat

def zapisat(m):
    nazov=input('Zadajte nazov suboru: ')
    f=open(nazov,'w')
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!=0:
                print((i,j),m[i][j],file=f)
    f.close()
    return None

def vypisat(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print('{:4d}'.format(m[i][j]),end='')
        print()
    return None

def scitat(c,d):
    q=[]
    for i in range(len(c)):
        temp=[]
        for j in range(len(c[0])):
            temp.append(c[i][j]+d[i][j])
        q.append(temp)
    return q

def odcitat(c,d):
    q=[]
    for i in range(len(c)):
        temp=[]
        for j in range(len(c[0])):
            temp.append(c[i][j]-d[i][j])
        q.append(temp)
    return q

def vloz(m,rm,roz):
    m=[]
    for i in range(roz):
            temp=[]
            for j in range(roz):
                x=rm.get((i,j),0)
                temp.append(x)
            m.append(temp)
    return m
        
############### HLAVNY PROGRAM ####################
a=[]
b=[]
c=[]
ra={}
rb={}
while 1==1:
    print('1.............nacitat matice')
    print('2.............vypisat matice')
    print('3.............scitat matice')
    print('4.............odcitat matice')
    print('5.............zapisat do suboru')
    print('0..............Koniec programu')
    volba=int(input())
    if volba==1:
        rozmer=int(input('Zadajte rozmer matice:'))
        ra=nacitat()
        rb=nacitat()
        a=vloz(a,ra,rozmer)
        b=vloz(b,rb,rozmer)
    elif volba==2:
        print('Prva matica:')
        vypisat(a)
        print()
        print('Druha matica:')
        vypisat(b)
    elif volba==3:
        c=scitat(a,b)
        vypisat(c)
    elif volba==4:
        c=odcitat(a,b)
        vypisat(c)
    elif volba==5:
        zapisat(a)
        zapisat(b)
    else:
        print('Koniec programu!')
        break
        
                
        
    
