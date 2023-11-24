def my_sort(liste):
    compteur = 0  # Initialisation du compteur d'échanges
    # Parcours de chaque élément de la liste
    for i in range(len(liste)):
        # Parcours de la liste - 1 fois (car on compare avec le suivant, le dernier n'en a pas)
        for j in range(len(liste) - 1):
            # Comparaison et échange si j est > à son voisin de droite
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]                
                # On fait monter le compteur à chaque échange
                compteur += 1  
    print("Nombre total de coups nécessaire pour trier la liste :", compteur)
    return liste


print(my_sort([12, 2, 55, 23, 102, 5]))
