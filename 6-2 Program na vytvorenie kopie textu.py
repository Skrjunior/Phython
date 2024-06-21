#Program na vytvorenie kopie textu
x=open('dva_prvy.txt', 'r')
cely = x.read()
x.close()

x=open('dva_prvy2.txt', 'w')
x.write(cely)
x.close()
