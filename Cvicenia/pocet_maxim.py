#PROGRAM na opakovane maximum
x=int(input('Zadajte cislo: '))
if x==0:
   pass
else:
   maxi=x
   pocet=1
   while x!=0:
      if x == maxi:
         pocet=pocet+1
      elif x > maxi:
         pocet=1
         maxi=x
      x=int(input('Zadajte cislo: '))
   print('Maximum je ',maxi,' nachadza sa ',pocet,'.krat')
      
