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

def zprava():
    text = input("Zadejte text zpravy:")

    a = 180
    cena = 3
    pocet_sms = len(text) // a

    if len(text) % a != 0:
         pocet_sms += 1
    return
    konecna_cena = pocet_sms * cena
        
    print(f"Cena sms je {konecna_cena} KC")

cislo = mobil()
if cislo is not None:
       zprava(cislo)
        