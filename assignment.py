# Program to determine division based on marks percentage


marks_percentage = int(input("Enter your marks percentage: "))
if marks_percentage >= 60:
    print("First Division")
elif marks_percentage >=50:
    print("Second Division")
elif marks_percentage >= 35:
    print("Third Division")
else:
    print("Fail")
