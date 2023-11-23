# Écrire un programme qui échange les valeurs de la première et de la dernière case
# d’une liste quelconque non vide.

liste = [12, 45, 61, 87, 99]

liste[0], liste[-1] = liste[-1], liste[0]

print(liste)