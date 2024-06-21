#PROGRAM na zistenie poctu slov vety a pocet slov s velkymi pismenami
ret=input('Zadajte vety ')
p=ret.split()
pv=0
pbodka=pciarka=potaznik=pvykricnik=0
print('Suvetia obsahuju ',len(p), ' slov')
for i in range(len(p)):
    slovo=p[i]
    if slovo[0]>='A' and slovo[0]<='Z':
        pv+=1
    if slovo[len(slovo)-1]=='.':
        pbodka+=1
    elif slovo[len(slovo)-1]==',':
        pciarka+=1
    elif slovo[len(slovo)-1]=='?':
        potaznik+=1
    elif slovo[len(slovo)-1]=='!':
        pvykricnik+=1
    
        
print('Pocet slov s velkymi pismenami je ',pv)
print('Pocet . je ',pbodka)
print('Pocet , je ',pciarka)
print('Pocet ? je ',potaznik)
print('Pocet ! je ',pvykricnik)


