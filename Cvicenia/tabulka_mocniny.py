#Program na vypis tabulky mocnin
zac=int(input('Zadajte zaciatok postupnosti: '))
hlavicka='Cislo | 2.moc | 3.moc  |  4.moc'
print('{:5}{:1}{:^6}{:1}{:^7}{:1}{:^9}'.format('Cislo','|',' 2.moc ','|',' 3.moc ','|','  4.moc '))
print('-'*len(hlavicka))
for i in range(zac,zac+10):
   print('{:5}{:7d}{:9d}{:11d}'.format(i,i**2,i**3,i**4))
