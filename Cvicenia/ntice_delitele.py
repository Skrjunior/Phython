#Program s funkciou na vypis delitelov cisla
def delitele(cislo):
   dd=()   #n-tica naplnana delitemi cisla
   for i in range(1,cislo+1):
      if cislo % i == 0:
         dd = dd + (i,)
   return dd   

#Hlavny program
x=int(input('Zadaj cislo '))
ntica=()
ntica=delitele(x)
print('Delite cisla ',x,' su ',ntica)
