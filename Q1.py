s1, s2, s3 = map(int, input("Enter the marks of the three subject: ").split())
avg = (s1  + s2 + s3) / 3
if avg > 40:
    print("Pass")
else:
    print("Fail")