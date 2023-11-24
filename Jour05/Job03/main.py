print ("Entrez la hauteur du triangle")
hauteur=int(input())
def triangle(hauteur):

    for i in range(hauteur - 1):
        espace = " " * (hauteur - i - 1)
        if i == 0:
            print(espace + "/\\")
        else:
            print(espace + "/" + " " * (2 * i) + "\\")

    base = "/" + "-" * (2 * hauteur - 2) + "\\"
    print(base)


triangle(hauteur)
