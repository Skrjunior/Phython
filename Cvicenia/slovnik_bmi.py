#BMI ludi
def bmi(hmotnost, vyska):
    return hmotnost/vyska/vyska

def hodnotenie(bmi):
    if bmi < 18:
        return "podvýživa"
    elif bmi < 22:
        return "v norme"
    else:
        return "nadváha"

def vypis(databaza):
    print("{:20} {:7} {:>10}".format("Meno", "BMI", "Hodnotenie"))
    print('-'*45)
    for meno, data in databaza.items():
        lok_bmi = bmi(data[0], data[1])
        lok_hodnotenie = hodnotenie(lok_bmi)
        print("{:20} {:>5.2f} {:>10}".format(meno, lok_bmi, lok_hodnotenie))

def nacitanie():
    meno='.'
    while meno!='':
        meno=input('Zadajte meno ')
        if meno=='':
            break
        if meno in databaza.keys():
            print('Meno uz v tabulke existuje!')
        else:
            pole=[]
            vaha=int(input('Zadajte vahu '))
            pole.append(vaha)
            vyska=float(input('Zadajte vysku '))
            pole.append(vyska)
            databaza[meno]=pole
    return databaza

######### HLAVNY PROGRAM #######################
databaza={}
databaza=nacitanie()
vypis(databaza)
x=input()


