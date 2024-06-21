# Program na odstranenie pismen zo slov
veta=input('Zadjte vetu: ')
veta2=''
for i in range(len(veta)):
   if (i%2!=0):
      veta2=veta2+veta[i]
print('Upravena veta:')
print(veta2)
