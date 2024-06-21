#Program na nahradu znakov vo vete
veta=input('Zadjte vetu: ')
veta2=''
p1=input('Zadajte znak, ktory sa ma zmenit: ')
p2=input('Zadajte znak, ktorym sa ma nahradzat: ')
for i in range(len(veta)):
   if veta[i] == p1:
      veta2=veta2+p2
   else:
      veta2=veta2+veta[i]
print('Upravena veta:')
print(veta2)
