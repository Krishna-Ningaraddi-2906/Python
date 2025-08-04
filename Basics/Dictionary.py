# Dictionary
# We use it when the order is not a big concern

chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types["Masala"])  # If i give the wrong key here it throws error

# Here if i give the wrong key it wont throw error instead it just prints empty string
print(chai_types.get("Ginger"))

chai_types["Ginger"] = "Sour"

print(chai_types)


for types in chai_types:
    # print(types)  # This prints the only keys
    print(types, " ", chai_types[types])

for key, values in chai_types.items():  # Here is fetches items means Masala : Spicy is one item
    print(key, values)
    if "Masala" in chai_types:
        print("I Have masala")

print(len(chai_types))

chai_types["Earl Grey"] = "citrus"

print(chai_types)

# In list we were not giving any input for pop here we need to give the key as input
print(chai_types.pop("Masala"))

# it gives the last item as output and it deletes the item completelty
print(chai_types.popitem())

chai_types_copy = chai_types.copy()  # It creates a new memory reference

print(chai_types_copy)

tea_shop = {
    "chai_variety": {
        "Masala": "Spicy",
        "Ginger": "Sour"
    },

    "price": {
        "Masala": 10,
        "Ginger": 20
    }
}

print(tea_shop)

# This gives chai_variety's value as out as it is a key
print(tea_shop["chai_variety"])
# It gives chai_variety key's inside ginger's value
print(tea_shop["chai_variety"]["Ginger"])

squared_num = {x: x**2 for x in range(6)}

print(squared_num)
keys = ["Masala", "Ginger", "Lemon"]

default_value = "Delicious"

# Here we are using dict method to construct a dictionary, where we are giving the keys are changing and
# default value is same value for all the keys
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
