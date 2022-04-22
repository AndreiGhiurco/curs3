def printGreeting():
    print('Buna ziua ! Bine ati venit')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua , {nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return(3.14)

#exercitiu:
#daca persoana este majora returnati true , altfel fals
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


    # zona de apelare, desktop
printGreeting()
printGreeting()
printGreetingByName('Sinpetrean ', 'Andy')
printGreetingByName('Sinpetrean ', 'Crina')
printGreetingByName('Sinpetrean ', 'Ares')
print(mediaNr(3,3,4))
print(piValue())
#se ia varsta utilizatorului
age = int(input('introduceti varsta dumneavoastra'))
if verificareMajor(age):
    print('cont creeat , bine ai venit')
else:
    print('nu aveti varsta necesara')

    #  oop
    #variabile => atributii, proprietati sau fields
    #functii => metode