#PROGRAM na sucet prevratenych hodnot
sucet=0
n=int(input('Zadajte cele cislo '))
for i in range(1,n+1):
   sucet=sucet + 1/i
print('Sucet postupnosti je ',sucet)
