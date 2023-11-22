def time_to_text(min):
    if min % 1 ==0:
        h = min // 60
        min = min % 60
        print (f"{h} heures et {min} minutes")
    else:
        print ("Il faut un nombre entier de minutes")

time_to_text(240)
time_to_text(222)
time_to_text(97)

