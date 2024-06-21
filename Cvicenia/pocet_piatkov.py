#Pocet piatkov mesiaca
pocet=int(input('Zadajte pocet dni '))
prvy=int(input('Zadajte 1. den mesiaca(0-6): '))
if prvy>4:
   piatok=0
else:
   piatok=1
while prvy<pocet:
   prvy=prvy+7
   piatok+=1

print('Mesiac ma ',piatok,' piatkov.')
   
   
