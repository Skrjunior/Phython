#Trojrozmerne pole
def nacitat():
   tp=[]
   r1=int(input('Zadajte 1.rozmer '))
   r2=int(input('Zadajte 2.rozmer '))
   r3=int(input('Zadajte 3.rozmer '))
   
   for i in range(r3):
      temp2=[]
      for j in range(r1):
         temp=[]
         for k in range(r2):
            hlaska='Prvok[',i,j,k,']'
            x=int(input(hlaska))
            temp.append(x)
         temp2.append(temp)
      tp.append(temp2)   
   return tp

def vypis(tp):
   for i in range(len(tp)):
      for j in range(len(tp[0])):
         for k in range(len(tp[0][1])):
            print(tp[i][j][k], end=' ')
         print()
      print()

#HLAVNY PROGRAM
pole=nacitat()
print('Vypis trojrozmerneho pola')
print('-'*25)
vypis(pole)
      
   
            
