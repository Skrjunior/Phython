#Program na nacitanie vyskytu znakov A,B,C v subore
subor=input('Zadajte nazov suboru: ')
f=open(subor,'r')
riadok=f.read()         #naraz nacita cely subor
pa=pb=pc=0
riadok=riadok.upper()   #zo vsetkych pismen urobi velke
print(riadok)
for i in range(0,len(riadok)-1):
    if riadok[i]=='A':
        pa=pa+1
    if riadok[i]=='B':
        pb=pb+1
    if riadok[i]=='C':
        pc=pc+1
print('Pocet a je ',pa, 'pocet b je ',pb,' pocet c je ',pc)
f.close()
        
