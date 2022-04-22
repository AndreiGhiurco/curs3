class ContBancar:
    # constructor
    def __init__(self, titularCont, iban):
        # atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0
        #metode

    def interogareSold(self):
        print(f'titular{self.titularCont}')
        print(f'iban{self.iban}')
        print(f'sold{self.sold}')
        print(f'activ{self.activ}')
        print(f'Nr. de incercari{self.incercari_activare}')
        print('_______________________________________')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('cared activat')
            self.activ = True
        else:
            print('PIN gresit')
            self.incercari_activare = self.incercari_activare + 1
            #self.incercari_activare +=1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'ati alimentat {suma}')
        print(f'aveti in cont {self.sold}')

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'ati cheltuit {suma}')
            print(f'aveti in cont {self.sold}')
        else:
            print('fonduri insuficiente!')

    def salut(self):
        print(f'buna {self.titular.Cont}')
