#PROGRAM na upravu vety
ret=input('Zadajte retazec ')
znak=input('Zadajte znak vymeny ')
pocet=0
ret2=''
for i in range(len(ret)):
   if ret[i] == znak:
      pocet += 1
      if pocet%2==0 and pocet%6!=0:
         ret2=ret2+znak+znak
      elif pocet%3==0 and pocet%6==0:
         pass
      elif ret2=ret2+znak
   else:
      ret2=ret2+ret[i]
print(ret2)
