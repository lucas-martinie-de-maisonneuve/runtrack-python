print ("Entrez un entier supérieur à 0")
N = int(input())

i=1
while i <=N:
    print (f"Table de multiplication de {i}:")
    j=1
    while j <=10:
        print (f"{i} x {j} = {i * j}")
        j += 1
    i += 1