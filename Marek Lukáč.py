
matVazHodnotM = []
matVahM = []
matHodnotyM = []
vazHodM = []
ziaciM = 10
parametreM = 10
vahM=1
pohM=1
verifikaciaM=1


for r in range(ziaciM):
    temp = []
    for s in range(parametreM):
        temp.append(0)
    matHodnotyM.append(temp)

if pohM == 1:
    print('matHodnoty'); print(matHodnotyM)

for r in range(vahM+1):
    temps = []
    for s in range(parametreM+1):
        temps.append(0)
    matVahM.append(temps)

if pohM == 1:
    print('matVah'); print(matVahM)

for r in range(ziaciM):
    tempq = []
    for s in range(parametreM+1):
        tempq.append(0)
    matVazHodnotM.append(tempq)

if pohM == 1:
    print('matVazHodnot'); print(matVazHodnotM)

o = open('data (1).txt', 'r', encoding='utf-8')
for r in range(ziaciM):
    riadok = o.readline().split()
    for s in range(parametreM):
        matHodnotyM[r][s] = riadok[s]
        if r>0:
            if s>0:
                matHodnotyM[r][s]= int(riadok[s])
            if s == parametreM:
                print(end="\n")
o.close()
print(end="\n")


if verifikaciaM == 1:
    print(matHodnotyM)
    print(end="\n")
if pohM ==1:
    print("...verifikacia ...mat Hodnôt.....","\n")

    for i in range(ziaciM):
        for j in range(parametreM):
            print(matHodnotyM[i][j], end="\t")
        print(end="\n")

o = open('data (1).txt', 'r', encoding='utf-8')
for r in range(vahM+1):
    riadok = o.readline().split()
    for s in range(parametreM):
        matVahM[r][s] = riadok[s]
        if r>0:
            if s>0:
                matVahM[r][s]= int(riadok[s])
            if s == parametreM:
                print(end="\n")
o.close()
print(end="\n")


if verifikaciaM == 1:
    print(matVahM)
    print(end="\n")
if pohM ==1:
    print("...verifikacia ...mat Váh.....","\n")

    for i in range(vahM+1):
        for j in range(parametreM+1):
            print(matVahM[i][j], end="\t")

print(end='\n')

for r in range(ziaciM):
    for s in range(parametreM):

        if r ==0:
            vazHodM[r][s]= matHodnotyM[r][s]
            vazHodM[r][parametreM]= 'SUMA'
        if r >0:
            if s == 0:
                vazHodM[r][s] = matHodnotyM[r][s]
        
            if s > 0: 
                vazHodM[r][s] = matHodnotyM [r][s]* matVahyM [l][s]
                 
print(end='\n')
print(end='\n')




print('data (1).txt', '\n')
for m in range(ziaciM):
    for n in range(parametreM +1):
        print(vazHodM[r][s], end='\t')
    print(end='\n')
print(end='\n')

#print('......Body pridelené žiakom(transformácia známok)....')
#for r in range (ziakov):
    #if r > 0:
        #if s > 0:
            #matHodnotyM[r][s] =6 - matHodnotyM[r][s]
       # print (matHodnotyM[r][s],end="\t")
     #print(end='\n')
     
#print(end='\n')

                
