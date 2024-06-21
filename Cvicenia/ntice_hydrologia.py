#Program na zistenie max, min z trojic n-tic (teplota,tlak,rosny_bod)
ntica=()
dni=3
for i in range(dni):
   hlaska=str(i+1)+'.den '
   ret=input(hlaska)
   ret=ret.strip()
   pozicia=ret.find(' ')
   tt=int(ret[:pozicia])  #teplota
   ret=ret[pozicia+1:]
   pozicia=ret.find(' ')
   tk=int(ret[:pozicia])  #tlak
   ret=ret[pozicia+1:]
   rb=float(ret)          #rosny bod
   pom=(tt,tk,rb,)
   ntica=ntica+(pom,)
print(ntica)
nt1=nt2=nt3=()
for i in range(dni):  #rozklad ntice na 3 ntice teplota,tlak,rosnybod
   nt1=nt1+(ntica[i][0],)
   nt2=nt2+(ntica[i][1],)
   nt3=nt3+(ntica[i][2],)
mintt=min(nt1)
maxtt=max(nt1)
mintk=min(nt2)
maxtk=max(nt2)
minrb=min(nt3)
maxrb=max(nt3)
print('Teplota min,max ',mintt,maxtt)
print('Tlak min,max ',mintk,maxtk)
print('Rosny bod min,max ',minrb,maxrb)

