print("Combien y a-t-il de marches ?")
marches = int(input())

print("Quelle est la hauteur des marches (en cm) ?")
hauteur = float(input())

def distance(marches, hauteur):
    largeur_marche = 0.2  #(20cm)
    trajet = (hauteur / 100 * marches * largeur_marche + 2) * 5 * 7 * 2     # + 2metres pour aller jusqu'au toilette
    print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {trajet:.2f} mètres par semaine.")

distance(marches, hauteur)