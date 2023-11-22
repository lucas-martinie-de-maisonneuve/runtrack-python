a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triangle équilatéral")
    elif a == b or a == c or b == c:
        print("Triangle isocèle")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Triangle rectangle")
    else:
        print("Triangle quelconque")
else:
    print("Pas de triangle possible")
