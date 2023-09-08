def bin(num):
    lst = []
    while num > 0:
        lst.append(num%2)
        num = num // 2
    for _ in lst:
        print(_, end = "")
bin(int(input("Enter the integer: ")))