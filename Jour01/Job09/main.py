nom = "Bananes"
prix = float(1.5)
quantite = 50

print (f"Il y a {quantite} {nom} en stock \n {prix}€ l'unité")

print ("Combien de bananes voulez vous acheter?")
achat = int(input())

quantite = quantite - achat
prix = prix * 1.1

print (f"Il reste désormais {quantite} {nom} en stock \n Avec 10% d'inflation, {"%.2f" % prix}€ l'unité")

