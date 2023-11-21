capital = 20000
taux = 0.02

annuel = capital * taux
print (f"Investissement de {capital}€")
print (f"Gain annuel : {annuel}€")

# Pour l'année suivante, on rajoute les 5000€ et les gains de l'année passé
# Le taux augente de 2%

capital = capital + 5000 + annuel
taux = taux + taux * 0.02 
annuel = capital * taux
print (f"Capital total: {capital}€")
print (f"Gain annuel : {"%.2f" % annuel}€")

# On enlève 10% du capital et le taux baisse de 1%

capital = capital * 0.9
taux = taux - taux*0.01
annuel = capital * taux
print (f"Après retrait de 10%, somme total: {capital}€")
print (f"Gain annuel : {"%.2f" % annuel}€")

# "%.2f" %  --> sert à n'afficher que 2 chiffres après la virgule 