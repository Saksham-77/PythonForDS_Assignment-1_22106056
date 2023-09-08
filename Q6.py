lst = []
usrnm = []
dmn = []
n = int(input("Enter the number of records you want to store: "))
for i in range(n):
    ID = input("Enter the email ID: ")
    lst.append(ID)
tup = tuple(lst)
for _ in tup:
    x = _.split("@")
    usrnm.append(x[0])
    dmn.append(x[1])
tup_usrnm = tuple(usrnm)
tup_dmn = tuple(dmn)
print(tup_usrnm, tup_dmn)