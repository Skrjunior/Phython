#PROGRAM na nacitanie 2 poli cifier zo suboru, porovnanie a scitanie dokopy a zapisu do suboru
def nacitanie():
    nazov=input('Zadajte nazov suboru ')                
    f=open(nazov,'r')
    ret=f.read()                                
    p=[]
    print(ret)
    for i in range(len(ret)):
        if ret[i]!='\n':
            p.append(int(ret[i]))
    f.close()
    return p

def vypis(a):
    for i in range(len(a)):
        print(a[i],end='')
    print()
    return None

def porovnanie(a,b):
    if len(a)!=len(b):
        print('Polia nemaju rovnaku velkost!')
    else:
        idx=0
        totozne=True
        for i in range(len(p1)):
            if p1[i]!=p2[i]:
                totozne=False
                idx=i
                break
        if totozne==True:
            print('Polia tvoria rovnake prvky. ')       
        else:                                              
            print('Polia sa lisia od ',idx,' prvku')   
    return None

def scitanie(p1,p2):
    p3=[]
    if len(p1)<len(p2):
        for i in range(len(p2)-len(p1)):
            p1.insert(0,0)
    elif len(p2)<len(p1):
        for i in range(len(p1)-len(p2)):
            p2.insert(0,0)
    prenos=0
    for i in range(len(p1)-1,-1,-1):
        p3.append((p1[i]+p2[i]+prenos)%10)
        prenos=(p1[i]+p2[i]+prenos)//10
    if prenos>0:
        p3.append(1)
    p3.reverse()

    return p3
                
#==============HLAVNA FUNKCIA =============================
p1=[]
p2=[]
p3=[]
p1=nacitanie()
p2=nacitanie()
print('Vypis prveho pola cisel')
vypis(p1)
print('Vypis druheho pola cisel')
vypis(p2)
porovnanie(p1,p2)
p3=scitanie(p1,p2)
print('Vysledok scitania je :')
vypis(p3)

            
