for i in range(2, 1001): 
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print (i)

# Ici on regarde si le reste de la division des nombres par j egale à 0 
# Si c'est le cas, on change de nombre 
# Si ce n'est pas le cas on les affichent
# On commence à 2 et on finit à i pour exclure 1 et i qui vérifirait la condition