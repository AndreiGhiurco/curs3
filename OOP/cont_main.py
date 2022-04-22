from OOP.cont_bancar import ContBancar

cont1 = ContBancar('Andy S', 'Ro001')
cont2 = ContBancar('Crina S', 'Ro002')

cont1.activareCont = (7777)
cont2.activareCont = (3333)
cont2.activareCont = (7777)

cont1.alimentareCont(300)
cont2.alimentareCont(300)
cont2.alimentareCont(700)


cont1.interogareSold()
cont2.interogareSold()

#tema :
#clasa angajat
#nume prenume salariu vechime functie
#constructor nume prenume salariu functie vechime
#metode == ce vechime ce functie ce salariu
#metoda de marire salariu in f de vechime
# actualizare vechime (marametru noua vechime)
    #    self.vechime = noua_vechime
#daca are vechime sub 5 ani marim cu 300 de lei ,  poeste 5 ani este 500 lei

