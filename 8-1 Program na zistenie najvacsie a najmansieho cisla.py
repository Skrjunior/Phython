#Program na zistenie najvacsie a najmansieho 
import random
randomList = []
for i in range(0, 20):
    randomList.append(random.randint(0, 1000))

print("Vypíš nahodne cisla")
print(randomList)
print("Vypíš najväčšie číslo")
print(max(randomList))
print("Vypíš najmenšie číslo")
print(min(randomList))
