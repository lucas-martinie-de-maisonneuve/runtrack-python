#Pyramide aller-retour mirroir

chaine = "abcdefghijklmnopqrstuvwxyz"


for j in range(10):
   
    i = 1
    
    while i <= len(chaine):
        k = (len(chaine) - i)*2
        print(chaine[:i], " " * k, chaine[::-1][:i])
        i += 2

    i = len(chaine) 
    while i > 0:
        k = (len(chaine) - i)*2
        print(chaine[:i], " " * k, chaine[::-1][:i])
        i -= 2
