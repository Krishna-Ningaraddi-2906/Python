# Tuple

# It is immutable we can't modify the tuple

tea_types = ("green", "black", "oolong")

# tea_types[0] = "Lemon"  # this throws error
print(tea_types[0])

# appart from this rest all the features are available in tuple as well

more_tea = ("Herbal", "Earl grey")

all_tea = tea_types + more_tea

print(all_tea)

# Here each element in the tuple is considered as variable and it is assigned
(black, green, oolong) = tea_types
# with the corresponding values in tea_types tuple
