# Strings
name = "krishna"
role = "hacker"


print(name, role)

# slicing

chai = "masala chai"

print(chai[0:6])

num_list = "0123456789"
print(num_list[0:])  # gives the entire string
print(num_list[-1])  # last element
print(num_list[0:5])  # prints till 0-4, 0 is included and 5 is excluded

# start from 0 hopps 2 element and prints till 5th pos o/p will be 024
print(num_list[0:5:2])

quote = "   Ideal mind is a devils workshop   "
print(quote.strip())  # removes all the leading and trailing spaces of the string

# replace

quote = quote.replace("Ideal", "ideal")

print(quote)

# Split

chai = "Lemon, Ginger, Mint, Masala"

types = chai.split(" ,")

print(types)

print(chai.find("Masala"))  # it gives o/p as 21 as M is positioned at 21st pos
print(chai.find("Ginger"))  # it gives o/p as 7 as G is positioned at 7th pos
# it gives o/p as -1 because there is no matching result found - case sensitive
print(chai.find("masala"))

# Count
print(chai.count("i"))


type = "Masala chai"
quantity = 2
order = "I Ordered {} cups of {} chai"  # {}  is called as place orders

print(order.format(quantity, type))


# List to string conversion

chai_variety = ["Lemon", "Masala", "Ginger"]
varieties = " ".join(chai_variety)  # this joines the list elements upon " "
print(varieties)


# length

print(len(chai))

# Here instead of '" "' we can use \--str--\ it print string along with " "
review = "krishna said, \"Masala chai is Awesome\""
print(review)

# Raw string here what ever the \n is used inside the string is not considered as next line instead it is considered as raw string
name = r"IamKrishna\nHacker"
print(name)
