def my_long_word(num, phrase):
    tri = ""
    mot = ""

    for i in phrase:
        if i != " " and i != ",":
            mot += i
        else:
            j = 0
        
            for n in mot:
                j += 1

            if j > num:
                tri += mot + " "

            mot = ""

    j = 0
    for n in mot:
        j += 1

    if j > num:
        tri += mot

    return tri

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))
