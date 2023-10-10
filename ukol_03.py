import json

body = {
    "Dušan Kadlec": 32,
    "Daniel Svoboda": 100,
    "Anežka Benešová": 17,
    "Andrea Vaňková": 15,
    "Robin Blažek": 100,
    "Renáta Tichá": 81,
    "Matyáš Vaněk": 23,
    "Tereza Procházková": 3,
    "Luboš Černý": 64,
    "Vasyl Novotný": 66,
    "Jaroslav Polák": 7,
    "Dušan Kříž": 63,
    "Vlasta Kadlecová": 20,
    "Zdenka Soukupová": 100,
    "Igor Krejčí": 95,
    "Stanislav Vaněk": 90,
    "Julie Poláková": 40,
    "Veronika Fialová": 53,
    "Květoslava Dvořáková": 52,
    "Ladislav Čermák": 76,
    "Dana Marková": 98,
    "Miloš Horák": 78,
    "Štefan Jelínek": 37,
    "Miloš Veselý": 25,
    "Aleš Kříž": 22,
    "Marcela Machová": 11,
    "Blanka Kučerová": 67,
    "Šárka Marešová": 81,
    "Dalibor Kadlec": 8,
    "Robert Pospíšil": 36
}

with open('body.json', mode='r', encoding='utf-8') as file:
    body_data = json.load(file)

znamka = {}
for klic, hodnota in body.items():
    if hodnota >= 60:
        znamka[klic] = "Pass"
    else:
        znamka[klic] = "Fail"

    print(f"{klic} ma znamku: {znamka[klic]}")

with open('prospech.json', mode='w', encoding='utf-8') as file:
    prospech_data = json.dump(znamka, file, ensure_ascii=False)

print("Soubor prospech.json byl úspěšně vytvořen.")
