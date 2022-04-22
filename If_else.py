piesa_faina = True

print('pornim radio')
if piesa_faina == False :
    print('dam mai tare')
    print('fredonam')
print(' oprim radio')

#if else
#daca numarul este par , printam acest lucru ,
# altfel printam impar

nr = 3
if nr % 2 == 0:
    print('nr par')

else :
    print('impar')

    # este un nr pozitiv
    if nr > 0 :
        print('pozitiv')
    else :
        print('nr nu este pozitiv')

# if, else if ,else ,
#  cum ne saluta robotelul in f de ora?
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int

ora = int(input('introdu ora'))
print( ora >0)
if (ora < 0 ):
    print('ora negativa')
elif (ora <= 11):
    print('buna dimineata')
elif (ora <= 18):
    print('buna ziua')
elif (ora <= 21):
    print('buna seara ')
elif (ora <= 24):
    print('noapte buna')

else :
    print('ora este mai mare decat 25')

#CTRL / selectam si deselectam ca sa nu apara in compilator
#robotel electronic

optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ales limb rom')
elif optiunea == 2:
    print('ales limb eng')
else:
    print('nu ati ales , mai incearca')


