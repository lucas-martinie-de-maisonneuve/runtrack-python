L = [8, 24,48,2,16]
j=0
for i in range(len(L)):
    if i % 3 == 0:
        j +=1

print (f"Il y a {j} multiple de trois dans la liste")