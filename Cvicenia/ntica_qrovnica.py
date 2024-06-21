#Program na vypocet kvadratickej rovnice
def rovnica(aa,bb,cc):
   korene=()
   if aa==0:
      korene=()
   else:
      dd=bb**2-4*aa*cc
      if dd <0:
         korene=()
      elif dd==0:
         x = -bb/(2*aa)
         korene=(x,)
      else:
         x=(-bb+dd)/(2*aa)
         y=(-bb-dd)/(2*aa)
         korene=(x,y)
   return korene
#Hlavny program
a=int(input('Zadajte koeficient a '))
b=int(input('Zadajte koeficient b '))
c=int(input('Zadajte koeficient c '))
ntica=rovnica(a,b,c)
if ntica==():
   print('Rovnica nema riesenie!')
else:
   print('Rovnica ma korene ',ntica)
