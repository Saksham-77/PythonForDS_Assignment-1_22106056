str = input("Enter the password: ")
up, lo = 0, 0
if len(str) < 5:
    print("The password must be at least 5 characters long.")
elif "&" not in str:
    print("The password must contain the '&' symbol.")
for i in str:
    if i.isupper():
        up += 1
    elif i.islower():
        lo += 1
if up >= 1 and lo >= 1 and len(str) >= 5 and "&" in str:
    print("Your password is correctly formatted.")
elif up == 0 and len(str) >= 5:
    print("The password must contain at least one uppercase alphabet.")
elif lo == 0 and len(str) >= 5:
    print("The password must contain at least one lowercase alphabet.")