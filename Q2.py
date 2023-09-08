lst1 = []
lst2 = []
n1, n2 = map(int, input("Enter the number of elements to be entered in the two lists: ").split())
for i in range(n1):
    x = input("Enter the element for list 1: ")
    lst1.append(x)
for _ in range(n2):
    z = int(input("Enter the element for list 2: "))
    lst2.append(z)
lst1.extend(lst2)
print(lst1)