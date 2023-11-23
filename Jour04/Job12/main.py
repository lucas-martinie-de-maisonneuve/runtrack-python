def tri(liste):
    n = 0
    for a in liste:
        n += 1

    for i in range(n):
        for j in range(n - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste

print(tri([12, 2, 55, 23, 102, 5]))
