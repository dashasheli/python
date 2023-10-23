def get_mobile_number():
    cislo = input("Zadej cislo mobilu: +420")
    if cislo.isdigit():
        if len(cislo) == 9:
            return cislo
        else:
            print("Chyba: potřeba zadat 9 číslic")
            return None
    else:
        print("Chyba: číslo mobilu musí být celé číslo.")
        return None

def zprava(cislo):
    text = input("Zadejte text zpravy:")
    a = 180
    cena = 3
    pocet_sms = len(text) // a
    if len(text) % a != 0:
        pocet_sms += 1
    konecna_cena = pocet_sms * cena
    print(f"Cena SMS je {konecna_cena} Kč")

cislo = get_mobile_number()

if cislo is not None:
    zprava(cislo)
