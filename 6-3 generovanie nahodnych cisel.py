#Program na vygerovanie nahodnych cisel
import random

subor=open('nahodne_cisla.txt', 'w')
for i in range(100):
    print(random.randint(1,100), file=subor)
subor.close()
