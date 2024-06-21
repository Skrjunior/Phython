#PROGRAM vlastnosti trojuholnikov pp,ps,pr
a=b=c=1
pr=ps=pp=0
while (a!=0 and b!=0 and c!=0):
    ret=input('Zadajte trojicu cisel ')
    while len(ret)>0 and ret.find(' ')>0:
        pozicia=ret.find(' ')
        a=int(ret[:pozicia])
        ret=ret[pozicia+1:]
        pozicia=ret.find(' ')
        b=int(ret[:pozicia])
        ret=ret[pozicia+1:]
        c=int(ret)
        print(a,b,c)
    if a!=0 and b!=0 and c!=0:
        if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
            pp=pp+1
        if (a==b) and (a==c):
            ps=ps+1
        if (a==b) and (a!=c) or (a==c) and (b!=c) or (b==c) and (a!=b):
            pr=pr+1
print('Pravouhlych:',pp,' rovnoramennych: ',pr,' rovnostrannych: ',ps)
    
