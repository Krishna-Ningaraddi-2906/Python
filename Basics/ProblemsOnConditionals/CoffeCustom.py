order_size = input("Enter the order size")
extra_shot = input("Confirm do you need extra short")

if extra_shot:
    coffee = order_size+"coffee with an extra short"
else:
    coffee = order_size+"Coffee"

print(coffee)
