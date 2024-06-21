#PROGRAM na zistenie poctu velkych pismen a medzier v retazci
ret=input('Zadajte vety.')
velke=0
medzery=0
for i in range(len(ret)):
   if 'A' <=ret[i] <='Z':
      velke=velke+1
   if ret[i] == ' ':
      medzery=medzery+1
print('Velkych pismen je ',velke,' a medzier ',medzery)
for i in range(len(ret)-1,-1,-1):
   print(ret[i],end='')
