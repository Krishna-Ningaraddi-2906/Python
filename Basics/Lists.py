# Lists

tea_varities = ["black", "green", "oolong", "white"]

print(tea_varities)
print(tea_varities[-1])
print(tea_varities[1:])
print(tea_varities[1:3])
print(tea_varities[:3])
print(tea_varities[1:3:2])

tea_varities[3] = "herbal"

print(tea_varities)

# tea_varities[1:2] = "Lemon"
# print(tea_varities)

tea_varities[2] = "Lemon"
print(tea_varities)

tea_varities[1:3] = ["Lemon", "Masala"]

print(tea_varities)

print(tea_varities[1:1])  # this gives []  bcz it starts at 1 and ends at 1

tea_varities[1:1] = ["test", "test"]
print(tea_varities)

tea_varities[1:3] = []
print(tea_varities)


for i in tea_varities:
    print(i)

for i in tea_varities:
    print(i, end="-\n")


tea_varities.append("oolong")

if "oolong" in tea_varities:
    print("Yes")
else:
    print("No")


# it removes the last value from the list, this gives the echo back
print(tea_varities.pop())

print(tea_varities)

#  this wont give the echo back to this gives the error
# print(tea_varities.remove("masala"))

tea_varities.remove("Masala")
print(tea_varities)

tea_varities.insert(1, "White")

print(tea_varities)


print(tea_varities.index("White"))  # returns the white's index value


tea_varities_copy = tea_varities.copy()


print(tea_varities, tea_varities_copy)

# this creates the list of 0-9 square numbers
squared_nums = [x**2 for x in range(10)]  # this is called as comprehensive

print(squared_nums)

# cube_nums = [for i in range(10) i**3]  # this won't work

print(cube_nums)
