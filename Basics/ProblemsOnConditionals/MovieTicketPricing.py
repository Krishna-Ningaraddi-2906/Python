# Q2 movie ticket pricing

age, day = input("Enter the age and day").split()
age = int(age)
if age >= 18:
    if day == "wednesday":
        print("price of ticket is 10$ ")
    else:
        print("price of ticket is 12$")
else:
    if day == "wednesday":
        print("price of ticket is 6$")
    else:
        print("price of ticket is 8$")

# This can be written as

age = int(input("Enter the age "))
day = input("Enter the day ")
price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print("Price for is ", price, "$")
