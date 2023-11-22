def moyenne(a, b, c):
    return (a + b + c) / 3

print("Entrez la première note :")
a = float(input())
print("Entrez la deuxième note :")
b = float(input())
print("Entrez la troisième note :")
c = float(input())

moyenne_etudiant = moyenne(a, b, c)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
