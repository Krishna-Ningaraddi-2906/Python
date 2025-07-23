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

# Type of data will be assigned to the allocated memory not the variable example a=10 here 10 will be stored in the
# memory and that memory allocation will be of number type so on and so forth

a = "krishna"

# here the value of a will be changed to krishna but back of the box garbage collector will not replace it
# immediately
# for numbers and string it will be bit late as compared to other datatypes

print(type(a))

# Here the value of l1 is changed and hence l2 is also changed because both are pointing to same reference

l1 = [1, 2, 3]
l2 = l1

print(l1)
print(l2)

l1[0] = 22

print(l1)
print(l2)

# Here both p1 and p2 are pointing to the same reference but i have changed the reference of p2 with the same values
# even though values are same in both p1 and p2 the reference is different any changes made in p1 will not affect the p2 and
# vice versa

p1 = [1, 2, 3]
p2 = p1

p2 = [1, 2, 3]

print(p1)
print(p2)

p1[0] = 33

print(p1)
print(p2)

# here initially both m and n are pointing to same reference so "==" and "is" both are true
# but when we explicitly give the new reference of same values as in m to n then "==" will be true but "is" will be false
# because both are pointing to different references as "=="checks value and "is" checks reference

m = [1, 2, 3]
n = m

print(m)
print(n)

print(m == n)  # True
print(m is n)  # True

n = [1, 2, 3]

print(m)
print(n)

print(m == n)  # True
print(m is n)  # False
