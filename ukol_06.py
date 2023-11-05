class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost=True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost

    def pujc_auto(self):
        if self.dostupnost:
            self.dostupnost = False
            return f"Potvrzuji zapůjčení vozidla {self.registracni_znacka}"
            self.dostupnost=False
        else:
            return f"Vozidlo {self.registracni_znacka} není k dispozici"
        
    def get_info(self):
        return f"Informace o vozidle {self.registracni_znacka}, typ: {self.typ_vozidla}, najeto: {self.najete_km} km"
    
    def __str__(self):
        return f"Potvrzuji zapůjčení vozidla {self.registracni_znacka}"

Auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

def dotaz():
    while True:
        znacka = input("Jakou značku auta si přejete půjčit? K dispozici jsou Peugeot nebo Škoda (pro ukonceni programu pouzijte 'konec'): ")
        if znacka.lower() == 'konec':
            break

        if znacka.lower() == "peugeot":
            print(Auto1.get_info())
            pujceni = input("Chcete si tento vůz půjčit? (ano/ne): ")
            if pujceni.lower() == "ano":
                print(Auto1.pujc_auto())
            else:
                print("Děkujeme, zkuste si vybrat něco jiného.")
        elif znacka.lower() == "škoda":
            print(Auto2.get_info())
            pujceni = input("Chcete si tento vůz půjčit? (ano/ne): ")
            if pujceni.lower() == "ano":
                print(Auto2.pujc_auto())
            else:
                print("Děkujeme, zkuste si vybrat něco jiného.")

        else:
            print("Omlouváme se, tato značka auta není k dispozici.")

dotaz()