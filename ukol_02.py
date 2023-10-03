sklad = {
  "N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

while True:
    product = input("Zadejte cislo produktu (pro ukonceni programu pouzijte 'konec'): ")

    if product.lower() == 'konec':
        break

    if product in sklad:
        pocet = int(input("Napiste pozadovany pocet produktu: "))

        if pocet <= sklad[product]:
            sklad[product] -= pocet
            print(f"Pocet produktu {product} byl snizen o {pocet} kusu. Aktualni pocet: {sklad[product]}.")
        else:
            print(f"Na sklade produkt {product} uz jen {sklad[product]} kusu. Zkuste znovu.")

    else:
        print("Produkt neexistuje.")
