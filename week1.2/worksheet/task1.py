# Worksheet 1.2: Task 1 Solution
grade = int(input("enter an integer grade in the range 0 to 100: "))

if grade >= 0 and grade <= 39:
    print(f"{grade} is a Fail")
elif grade >= 40 and grade <= 69:
    print(f"{grade} is a Pass")
elif grade >= 70 and grade <= 100:
    print(f"{grade} is a Distinction")
else:
    print("Error: Grade must be an integer between 0 and 100")

