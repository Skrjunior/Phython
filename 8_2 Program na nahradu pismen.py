#Program na nahradenie pismen
veta=input('Zadaj goraliky na nahrdelniku: ')
veta2=''
p1='A'
p2=('***')
for i in range(len(veta)):
   if veta[i] == p1:
      veta2=veta2+p2
   else:
      veta2=veta2+veta[i]
print('Upraveny nahrdelnik:')
print(veta2)
