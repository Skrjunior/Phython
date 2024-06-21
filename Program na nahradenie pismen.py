#Program na nahradenie pismen
retazec=input('Zadaj retazec: ')
for i in retazec:
    if (i >= 'a' and i <= 'z'):
        print(i.upper())
    else:
        print(i.lower())
