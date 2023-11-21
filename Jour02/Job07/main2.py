chaine = "abcdefghijklmnopqrstuvwxyz"*3

for j in range(10):
   
    i = 1
    while i <= len(chaine):
        print(chaine[:i])
        i += 2

    i = len(chaine) 
    while i > 0:
        print(chaine[:i])
        i -= 2
