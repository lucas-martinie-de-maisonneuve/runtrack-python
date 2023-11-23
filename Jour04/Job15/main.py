L=[22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def tri(liste):
    n = 0
    for a in liste:
        n += 1

    i = 0
    while i < n:
        liste[i] = int(liste[i] + 0.5)
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
            j += 1
        i += 1
    return liste

print(tri(L))
