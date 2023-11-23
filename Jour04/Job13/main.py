L=[10,20,30,20,10,50,60,40,80,50,40]
M=[]
for i in L:
    if i not in M:
        M = M + [i]

print(M)
