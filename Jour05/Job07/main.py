def arrondir(notes):
    arrondie = []
    echec = []
    for note in notes:
        if note < 40:
            echec.append(note)
        else:
            hausse = ((note // 5) + 1) * 5
            if hausse - note < 3:
                arrondie.append(hausse)
            else:
                arrondie.append(note)

    print("Notes d'origine :", notes)
    print("Notes arrondies :", arrondie)
    if echec != []:
        print(f"{len(echec)} échec(s) au test avec {echec}")
    else:
        print("Aucun échec au test.")


arrondir([83, 72, 45, 38, 93, 48, 32])


