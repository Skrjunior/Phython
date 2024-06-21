#Program na prevody bin-dec a dec-bin
def fnc_twoToTen(cislo):
    y=0
    for i in range(len(str(cislo))):   
        z=cislo%2
        y=y+2**i*z
        cislo=cislo//10
    return y

while True:
   x=input('Zadajte cislo ')
   if x!='':
       if x.count('b')>0:
           je_bin=True
           for i in range(2,len(x)):
               if x[i] not in ['0','1']:
                   print('Nie je binarna reprezentacia cisla!')
                   je_bin=False
           if je_bin==True:
               cc=int(x[2:])
               print('Dekadicka reprezentacia ',fnc_twoToTen(cc))
       else:
           print('Binarna reprezentacia ',bin(int(x)))
   else:
       break
