# Step 1: Create a dictionary of student marks
student_marks = {
    "Aliya": 74,
    "Bhupesh": 90,
    "Chitransh": 78
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")