def produit(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucun produit correspondant")

produit("fruits", "hiver")
produit("fruits", "ete")
produit("legume", "hiver")
produit("legume", "ete")
produit("fruits", "printemps")