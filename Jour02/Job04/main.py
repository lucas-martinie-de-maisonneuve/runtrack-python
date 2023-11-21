def positif(x):  #On definit 'positif'
    return x > 0

while True:
    try:
        N = int(input("Entrez un entier supérieur à 0 : "))
#Si notre input est un entier positive
        if positif(N):
            for i in range(1, N + 1):
                print(f"Table de multiplication de {i}:")
                for j in range(11):
                    print(f"{i} x {j} = {i * j}")
            break

        else:
            print("Le nombre doit être supérieur à 0. Veuillez réessayer.") #Si l'input n'est pas pas positive ou égal à 0
    except ValueError:
        print("Veuillez entrer un nombre entier valide.") # Si notre input est un texte