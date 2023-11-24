def draw_rectangle(l, h):
    l = l - 2
    h = h - 2
    print("|" + "-" * l +"|")

    for i in range(h):
        print("|" + " " * (l) + "|")

    print("|" + "-" * l +"|")

draw_rectangle(10, 3)
