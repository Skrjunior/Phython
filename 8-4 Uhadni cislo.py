#Program uhadni cislo
import random
suc=0
x=random.randint(1,100)
print(x)
for i in range(1,100):
    a=int(input('Zadaj cislo: '))
    if(a<x):
        print('Netrefil si, zadaj väcsie cislo!')
    elif(a>x):
        print('Netrefil si, zadaj mensie cislo!')
    else:
        print('Uhadol si cislo')
        suc=suc+i
        print('Potreboval si ',suc,'pokusov.')
        break       
