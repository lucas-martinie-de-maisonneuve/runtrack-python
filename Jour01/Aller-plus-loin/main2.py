print ("Entrer une chaine de caractère")
chaine = input()

if 'e' in chaine:    
    compter = chaine.count("e")
    print (f"Il y a {compter} 'e' dans cette chaine")
else:
    print ("Il n'y a pas de e")
