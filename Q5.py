str = input("Enter the numbers: ")
splt = str.split()
lst = []
for i in splt:
    lst.append(int(i))
for _ in range(len(lst)):
    for j in range(_, len(lst)):
        if lst[_] > lst[j]:
            temp = lst[_]
            lst[_] = lst[j]
            lst[j] = temp
print(lst)
