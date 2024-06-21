#Program na vyradenie opakujucich a cisel z klavesnice
ret=input('Zadajte cisla ')
vys=()
while (len(ret)>0 and ret.count(' ')>0):
   pozicia=ret.find(' ')
   cislo=int(ret[:pozicia])
   vys=vys+(cislo,)
   ret=ret[pozicia+1:]

vys2=()
for p in vys:
   if p not in vys2:
      vys2=vys2+(p,)
print(vys2)   
