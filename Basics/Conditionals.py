# Grade Calculator

score = int(input("Enter the marks "))
grade = ''

if (score > 100):
    print("Please Enter the valid score")
    exit()

if (score >= 90):
    grade = 'A'
elif (score >= 80):
    grade = 'B'
elif (score >= 70):
    grade = 'C'
elif (score >= 60):
    grade = 'D'
elif (score < 60):
    grade = 'F'

print("Your grade is ", grade)
