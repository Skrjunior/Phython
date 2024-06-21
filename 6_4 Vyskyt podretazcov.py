#Program na zistenie vzskytu podretaycov
def pocet_vyskytov(podretazec, retazec):
    pocet = 0
    for ix in range(len(retazec)):
        if retazec[ix:ix+len(podretazec)] == podretazec:
            pocet += 1
    return pocet
