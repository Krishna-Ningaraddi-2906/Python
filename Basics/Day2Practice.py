# In python everything is refered as objects so when ever the we create a any variable python treats it as an object
# So the reference of that memory location will be stored in that variable when ever we change the value of that variable
# python creates a new object with new reference and it will be stored in that variable without changing anything in the previous
# object, python has a inbuilt garbage collector when it check that there are no references to the object it will delete it


# Example

a = 10
b = a

print(a)
print(b)

# Here i have changed the value of a but still the value of b is as before i.e 10
a = 20

print(a)
print(b)

# Strings

string1 = "Krishna"
String2 = "Hustler"

print(string1+" "+String2)

string3 = string1+" "+String2

print(string1[1:4])
