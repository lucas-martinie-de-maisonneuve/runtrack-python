nom = "Bananes"
prix = float(1.5)
quantite = 10

print ("Il y a", quantite, nom, "en stock")
print (prix, "€ l'unité")
print ("Combien de bananes voulez vous acheter?")
achat = int(input())

quantite = quantite - achat

prix = prix * 1.1

print ("il y'a maintenant", quantite, nom, "en stock")
print (prix, "€ l'unité")
