#Program na zistenie poctu cifier a pocetnost vyskytov jednotlivych cifier
#x='1234567899999999999999999999999999999999987878784545454151212'
x=input('Zadajte velmi dlhe cislo ')
p=[0,0,0,0,0,0,0,0,0,0]   
for i in range(len(x)):
     idx=int(x[i])
     p[idx]=p[idx]+1
for i in range(0,10):
     if p[i]>0:
          print(i,'-',p[i])
