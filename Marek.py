
matVazHodnot = []
matVah = []
matHodnoty = []
vazHod = []
ziaci = 10
parametre = 10
vah=1
poh=1
verifikacia=1


for r in range(ziaci):
    temp = []
    for s in range(parametre):
        temp.append(0)
    matHodnoty.append(temp)

if poh == 1:
    print('matHodnoty'); print(matHodnoty)

for r in range(vah+1):
    temps = []
    for s in range(parametre+1):
        temps.append(0)
    matVah.append(temps)

if poh == 1:
    print('matVah'); print(matVah)

for r in range(ziaci):
    tempq = []
    for s in range(parametre+1):
        tempq.append(0)
    matVazHodnot.append(tempq)

if poh == 1:
    print('matVazHodnot'); print(matVazHodnot)

o = open('data (1).txt', 'r', encoding='utf-8')
for r in range(ziaci):
    riadok = o.readline().split()
    for s in range(parametre):
        matHodnoty[r][s] = riadok[s]
        if r>0:
            if s>0:
                matHodnoty[r][s]= int(riadok[s])
            if s == parametre:
                print(end="\n")
o.close()
print(end="\n")


if verifikacia == 1:
    print(matHodnoty)
    print(end="\n")
if poh ==1:
    print("...verifikacia ...mat Hodnôt.....","\n")

    for i in range(ziaci):
        for j in range(parametre):
            print(matHodnoty[i][j], end="\t")
        print(end="\n")

o = open('data (1).txt', 'r', encoding='utf-8')
for r in range(vah+1):
    riadok = o.readline().split()
    for s in range(parametre):
        matVah[r][s] = riadok[s]
        if r>0:
            if s>0:
                matVah[r][s]= int(riadok[s])
            if s == parametre:
                print(end="\n")
o.close()
print(end="\n")


if verifikacia == 1:
    print(matVah)
    print(end="\n")
if poh ==1:
    print("...verifikacia ...mat Váh.....","\n")

    for i in range(vah+1):
        for j in range(parametre+1):
            print(matVah[i][j], end="\t")

print(end='\n')

for r in range(ziaci):
    for s in range(parametre):

        if r ==0:
            vazHod[r][s]= matHodnoty[r][s]
            vazHod[r][parametre]= 'SUMA'
        if r >0:
            if s == 0:
                vazHod[r][s] = matHodnoty[r][s]
            if s > 0: 
                vazHod[r][s] = matHodnoty[r][s]* matVahy[l][s]
                 
print(end='\n')
print(end='\n')


print('data (1).txt', '\n')
for m in range(ziaci):
    for n in range(parametre +1):
        print(vazHod[m][n], end='\t')
    print(end='\n')
print(end='\n')

                
