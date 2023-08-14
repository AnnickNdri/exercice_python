mot = "modifier"

resultat = ""
for i, lettre in enumerate(mot):
    if i % 3 == 0:
        resultat += lettre.upper()
    else:
        resultat += lettre.lower()

print(resultat)
