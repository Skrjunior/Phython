#Program na vypísanie deliteľov
cislo = int(input('Zadaj číslo: '))
print('delitele:', end=' ')
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:    
        print(delitel, end=' ')
print()
