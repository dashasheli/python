teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvoř seznam průměrných teplot pro každý den.
# Vytvoř seznam ranních teplot.
# Vytvoř seznam nočních teplot.
# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

avg_teploty = [round(sum(t) / len(t)) for t in teploty]
print(f"Prumerne teploty jsou: {avg_teploty}")

ranni_teploty = [t[0] for t in teploty]
print(f"Ranni teploty jsou: {ranni_teploty}")

nocni_teploty = [t[3] for t in teploty]
print(f"Nocni teploty jsou: {nocni_teploty}")

dalsi_teploty = [[t[1], t[3]] for t in teploty]
print(f"Poledni a nocni teploty jsou: {dalsi_teploty}")