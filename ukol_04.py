import math

def mobil():
    cislo = input("Zadej cislo mobilu: +420")

    if cislo.isdigit():
        if len(cislo) == 9:
            return cislo
        else:
            print("Chyba: potreba zadat 9 cislic")
            return None
    else:
        print("Chyba: cislo mobilu musi byt cele cislo.")
        return None

cislo = mobil()
if cislo is not None:
    
    def zprava():
        text = input("Zadejte text zpravy:")

        a = 180
        cena = 3
        pocet_sms = len(text) // a

        if len(text) <= a:
            konecna_cena = cena
        else:
            konecna_cena = math.floor(pocet_sms * cena) + cena
        print(f"Cena sms je {konecna_cena} KC")
        
    zprava()