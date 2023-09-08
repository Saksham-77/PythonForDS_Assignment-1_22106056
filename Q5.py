str = input("Enter the numbers: ")
splt = str.split()
lst = []
for i in splt:
    lst.append(int(i))
for _ in range(0, len(splt)):
    m = min(lst[_:])
    if lst[_] == m:
        pass
    else:
        index = lst.index(m)
        lst[index] = lst[_]
        lst[_] = m
print(lst)
