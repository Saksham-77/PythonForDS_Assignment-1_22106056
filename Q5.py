str = input("Enter the numbers: ")
splt = str.split()
for _ in range(0, len(splt)):
    if _ == len(splt) - 1:
        break
    else:
        m = min(splt[_:])
        indx = splt.index(m)
        splt[indx] = splt[_]
        splt[_] = m
print(splt)