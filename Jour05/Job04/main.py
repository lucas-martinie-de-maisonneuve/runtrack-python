def diago(n):
    a = "+" + "-" * (n+1) + "+"
    print(a)

    for i in range(n + 1):
        b = "#" * (n + 1)
        liste = list(b)
        if i < len(liste):
            liste[-i - 1] = " "
        c = ""
        for diese in liste:
            c = c + diese
        print("|"+c+"|")

    print(a)

diago(5)
