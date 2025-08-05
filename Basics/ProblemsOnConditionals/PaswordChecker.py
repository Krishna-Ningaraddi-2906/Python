password = input("Enter the password ")

length = len(password)

if (length < 6):
    print("Weak pwd")
elif (length <= 10):
    print("Medium")
else:
    print("Strong")
