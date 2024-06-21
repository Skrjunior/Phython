#Program ktory precita vstupny subor a zisti z neho minimum a maximum.

nazov=input('Zadajte nazov suboru ')
f=open(nazov,'r')
for ret in f:
    maxi=-10000000000000
    mini=999999999999999
    print(ret, end='')    #2xenter   
    while (len(ret)>0) and (ret.count(' ')>0):
        ix = 0
        ix=ret.find(' ')
        cislo=int(ret[:ix])   #od zaciatku po medzeru urobi cislo
        if cislo>maxi:
            maxi=cislo
        if cislo<mini:
            mini=cislo
        ret2=ret[ix+1:]      #vymazanie retazca po medzeru
        ret=ret2
    if (len(ret)>0):          #zostatok retazca je este cislo
        cislo=int(ret[:len(ret)])
        if cislo>maxi:
            maxi=cislo
        if cislo<mini:
            mini=cislo
    print('Minimum je ',mini,' a maximum je ',maxi)            

f.close()

