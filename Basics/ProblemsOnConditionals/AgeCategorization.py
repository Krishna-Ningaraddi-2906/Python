# Q1 Age categorization


def ageCategorization(age):
    if (age < 13):
        return "child"
    elif age < 20:
        return "Teenage"
    elif age < 60:
        return 'Adult'
    else:
        return "Senior"


age = int(input("Enter the age "))
print(ageCategorization(age))
