#Funkcia na obratenie slova   
def fnc_reverseWord(s):             
    s2=''                       
    for i in range(len(s)-1,-1,-1):
        s2=s2+s[i]
    return s2

####### HLAVNY PROGRAM ##########        
s=input('Zadajte vetu ')
while len(s)>0 and s.find(' ')>0:
    p=s.find(' ')
    w=s[:p]
    s2=fnc_reverseWord(w)
    print(s2, end=' ')
    s=s[p+1:]

if len(s)>0:
    s2=fnc_reverseWord(s)
    print(s2)


  
