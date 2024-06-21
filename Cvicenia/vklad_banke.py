#PROGRAM na vypocet urokov
x=int(input('Zadajte vklad '))
p=float(input('Zadajte urok '))
ciel=int(input('Zadajte cielovu sumu '))
vys=x
for i in range(10):
   vys=vys+vys*p/100
print('Nasporene za 10 rokov: ',vys)
vys=x
roky=0
while vys<ciel:
   vys=vys+vys*p/100
   roky=roky+1
print('Cielovu sumu dosiahnete za ',roky,'rokov')
   
