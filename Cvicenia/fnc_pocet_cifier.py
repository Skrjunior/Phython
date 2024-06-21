#FUNKCIA na zisteni poctu cifier cisla
def fnc_pocet_cifier(cislo):
    p=0
    if cislo<0:
        cislo=abs(cislo)
    if cislo == 0:
        p=1
    else:
        while cislo>0:
            cislo = cislo //10
            p=p+1
    return p


