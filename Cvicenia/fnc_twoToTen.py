#Funkcia na prevod dvojkoveho cisla na desiatkove
def fnc_twoToTen(cislo):
    y=0
    for i in range(len(str(cislo))):
        z=cislo%2
        y=y+2**i*z
        cislo=cislo//10
    return y
