student_name = input("Enter student name: ")
subject1 = float(input("Enter first subject mark: "))
subject2 = float(input("Enter second subject mark: "))

average_mark = (subject1 + subject2) / 2
result = "Pass" if average_mark >= 50 else "Fail"

print(f"Student Name: {student_name}")
print(f"Average Mark: {int(average_mark) if average_mark.is_integer() else average_mark}")
print(f"Result: {result}")
