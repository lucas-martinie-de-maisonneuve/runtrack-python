capital = 20000
rendement = 0.01

annuel = capital * rendement * 12
print ("Investissement de", capital, "€")
print ("Gain annuel :", annuel, "€")


rendement = rendement + 0.02 
capital = annuel + capital + 5000
annuel = capital * rendement * 12
print ("Après rajout de 5000 €, somme total:", capital, "€")
print ("Gain annuel :", annuel, "€")

rendement = rendement - 0.01
capital = (annuel + capital) * 0.9
annuel = capital * rendement * 12
print ("Après retrait de 10%, somme total:", capital, "€")
print ("Gain annuel :", annuel, "€")