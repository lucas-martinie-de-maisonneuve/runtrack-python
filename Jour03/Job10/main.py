def posneg (nombre):

    if nombre > 0 and nombre % 1 == 0:
        if nombre % 2 == 0:
            print (nombre, "est pair")
        else:
            print (nombre, "est impair")
    else:
        print ("Le nombre n'est pas entier ou alors égal à 0")

posneg(2)
posneg(41)
posneg(7)
posneg(48)
posneg(0)
posneg(2.2)