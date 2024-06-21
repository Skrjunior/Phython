#Program na zistenie 1,2,3 maxima a minima z cisel.
x=input('Zadajte cisla oddelene medzerou  ')
p2=[]
          #x='1 2 3 5 -10 11 -100 99 55 44 77'
p2=x.split()
p=[]
for i in range(len(p2)):
     p.insert(i,int(p2[i]))   #p=[1,2,3,5,-10,11,-100,99,55,44,77]

p.sort()
print('Maxima: ',p[-1],p[-2],p[-3])
print('Minima: ',p[0],p[1],p[2])
     
