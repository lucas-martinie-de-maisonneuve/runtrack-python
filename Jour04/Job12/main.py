def tri(liste):
    n = 0
    for a in liste:
        n += 1
        
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
            j += 1
        i += 1
    return liste

print(tri([12, 2, 55, 23, 102, 5]))
