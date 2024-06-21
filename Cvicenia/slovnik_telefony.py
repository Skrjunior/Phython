#Program na slovnik - telefonny zoznam
def pridat_polozku():
    kluc=int(input('Zadajte cislo '))
    if kluc in tel.keys():
        print('Cislo uz v zozname existuje!')
    else:
        hodnota=[]
        meno=input('Zadajte meno ')
        adresa=input('Zadajte adresu ')
        hodnota.append(meno)
        hodnota.append(adresa)
        tel[kluc]=hodnota
    return None

def vypisat_zoznam(z,vystup):
    if vystup==0:   #VYPIS na obrazovku
        f=None
    else:           #Zapis do suboru
        nazov=input('Zadajte nazov suboru ')
        f=open(nazov,'w')
    print('{:^62s}'.format('TELEFONNY ZOZNAM'),file=f)
    print('='*62,file=f)
    for kluc,hodnota in z.items():
        print('{:010d}{:s}{:20s}{:30s}'.format(kluc,'  ',hodnota[0],hodnota[1]),file=f)
    if vystup==1:
        f.close()
        
    return None

def zrusit_polozku(z):
    kluc=int(input('Zadajte cislo zoznamu '))
    if kluc in z.keys():
        del z[kluc]
        print('Zmazal som polozku s cislom ',kluc)
    else:
        print('Zadane cislo neexistuje v zozname ')

def opravit_polozku(z):
    kluc=int(input('Zadajte cislo zoznamu '))
    if kluc in z.keys():
        pom=input('Zadajte polozku na opravu M/A ')
        if pom.upper()=='M':
            meno=input('Zadajte meno ucastnika ')
            z[kluc][0]=meno
        elif pom.upper()=='A':
            adresa=input('Zadajte adresu ucastnika ')
            z[kluc][1]=adresa
        else:
            pass
    else:
        print('Zadane cislo neexistuje v zozname!')
    

#################  HLAVNY PROGRAM ##############
tel={}
while 1==1:
    print()
    print('1...........nova polozka')
    print('2...........vypis zoznamu')
    print('3...........zapis do suboru')
    print('4...........zrusit polozku')
    print('5...........opravit polozku')
    print('0...........koniec programu')
    volba=int(input())
    if volba==1:
        pridat_polozku()
    elif volba==2:
        vypisat_zoznam(tel,0)
    elif volba==3:
        vypisat_zoznam(tel,1)
    elif volba==4:
        zrusit_polozku(tel)
    elif volba==5:
        opravit_polozku(tel)
    else:
        print('Koniec programu!')
        break
        
