#Program na evidenciu uchadzacov
def novy_uchadzac():
    cislo=int(input('Zadajte cislo uchadzaca '))
    if cislo in evidencia.keys():
        print('Uchadzac s tymto cislom uz existuje!')
    else:
        temp=[]
        priezvisko=input('Zadajte priezvisko ')
        temp.append(priezvisko)
        meno=input('Zadajte meno ')
        temp.append(meno)
        suma=0
        temp.append(suma)
        program=input('Zadajte studijny program ')
        temp.append(program)
        while (program != '' and len(program)>0):
            program=input('Zadajte studijny program ')
            if program == '' and len(program)==0:
                break
            else:
                temp.append(program)
        suma=int(input('Zadajte zaplatenu sumu '))
        temp[1]=suma
        evidencia[cislo]=temp
    return 0

def vypis_uchadzacov(device):
    if device == 0:    #vypis na obrazovku
        f=None
    else:
        nazov=input('Zadajte nazov suboru na zapis ')
        f=open(nazov,'w')
    print('{:>4}{:1}{:<10}{:<10}{:>4}{:1}{:<10}'.format('Cislo',' ','Priezvisko','Meno','Suma',' ','Programy'),file=f)
    print(55*'=', file=f)
    for cislo,temp in evidencia.items():
        print('{:>4}{:1}{:<10}{:<10}{:>4}'.format(cislo,' ',temp[0],temp[1],temp[2]),end=' ',file=f)
        for i in range(len(temp)-3):
            print(temp[i+3],end=' ',file=f)
        print(file=f)
    if device == 1:
        f.close()

def oprava_uchadzaca():
    cislo=int(input('Zadajte cislo na opravu '))
    if cislo not in evidencia.keys():
        print('Cislo uchadzaca nie je v evidencii!')
    else:
        pole=[]
        pole=evidencia[cislo]
        polozka=input('Zadajte polozku opravy Priezvisko/P, Meno/M, Sumu/S, St.program/R')
        if polozka == 'P':
            priezvisko=input('Zadajte nove priezvisko ')
            evidencia[cislo][0]=priezvisko
        elif polozka == 'M':
            meno=input('Zadajte nove priezvisko ')
            evidencia[cislo][1]=meno
        elif polozka == 'S':
            suma=int(input('Zadajte novu sumu '))
            evidencia[cislo][1]=suma
        elif polozka == 'R':
            evidencia[cislo][3:]=[]    
            temp=[]
            while True:
                program=input('Zadajte nove programy ')
                if program!='' and len(program)>0:
                   temp.append(program)
                else:
                    break
            for i in range(len(temp)):
                evidencia[cislo].append(temp[i])

def zmazanie_uchadzaca():
    cislo=int(input('Zadajte cislo uchadzaca '))
    if cislo in evidencia.keys():
        del evidencia[cislo]
    else:
        print('Uchadzac s cislom ',cislo,' nie je v evidencii!')

def nacitat_subor():
    nazov=input('Zadajte nazov suboru ')
    f=open(nazov,'r')
    for ret in f:
        if ret[ :5]=='Cislo':
            continue
        else:
            pole=[]
            pole=ret.split()
            cislo=pole[0]
            if cislo in evidencia.keys():
                continue
            else:
                temp=[]
                temp=pole[1:]
                evidencia[cislo]=temp
    f.close()

################## HLAVNY PROGRAM #########################
evidencia={}
while True:
    print('Novy uchadzac ..........1')
    print('Vypis uchadzacov........2')
    print('Oprava uchadzaca........3')
    print('Zmazanie uchadzaca......4')
    print('Zapis do suboru.........5')
    print('Nacitanie zo suboru.....6')
    print('Koniec..................0')
    volba=int(input())
    if volba == 1:
        novy_uchadzac()
    elif volba == 2:
        vypis_uchadzacov(0)
    elif volba == 3:
        oprava_uchadzaca()
    elif volba == 4:
        zmazanie_uchadzaca()
    elif volba == 5:
        vypis_uchadzacov(1)
    elif volba == 6:
        nacitat_subor()
    else:
        print('Koniec programu ......')
        break
    
