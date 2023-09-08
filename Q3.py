str = input("Enter the string: ")
cpt = ""
splt = str.split()
for _ in splt:
    cpt = cpt + _[0].upper() + _[1 : ] + " "
print(cpt)