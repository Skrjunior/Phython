#Program na zistenie poctu slov konciaich na a,A - vystup bude n-tica
def zisti_slova(veta):
   ntica=()
   while (len(veta)>0 and veta.count(' ')>0):
      pozicia=veta.find(' ')
      if veta[pozicia-1].upper() in ('A'):
         ntica=ntica+(veta[:pozicia],)
      veta=veta[pozicia+1:]
   return ntica

#Hlavny program
ret=' '
print('Program sa skonci po zadani prazdnej vety! ')
while len(ret)>0:
   ret=input('Zadajte vetu ')
   if len(ret)==0:
      pass
   else:
      nt=zisti_slova(ret)
      print('Slova konciace na a,A: ',nt)
