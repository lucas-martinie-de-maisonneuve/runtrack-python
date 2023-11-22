def time_to_text(min):
      
    h = min // 60
# On créé une variable qui récupère sans le reste une fois divisé par 60
    m = min % 60
# On créé une deuxième variable qui récupère le reste
    print (f"{h} heures et {m} minutes")

time_to_text(240)
time_to_text(222)
time_to_text(97)

