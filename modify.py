def modif_element(liste, anc_valeur, nouv_valeur):
    for i, element in enumerate(liste):
        if isinstance(element, list):
            modif_element(element, anc_valeur, nouv_valeur)
        elif element == anc_valeur:
            liste[i] = nouv_valeur

list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
anc_valeur = 58
nouv_valeur = 5800

modif_element(list1, anc_valeur, nouv_valeur)
print(list1)
