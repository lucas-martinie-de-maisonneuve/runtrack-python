def draw_rectangle(long, haut):
    long = long - 2
    haut = haut - 2
    print("|" + "-" * long +"|")

    for i in range(haut):
        print("|" + " " * (long) + "|")

    print("|" + "-" * long +"|")

draw_rectangle(10, 3)
