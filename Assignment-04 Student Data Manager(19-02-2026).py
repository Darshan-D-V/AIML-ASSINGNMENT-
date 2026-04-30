# Store data for 5 students using dictionaries

students = {}

# Taking input
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Finding topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Calculating class average
average = sum(students.values()) / len(students)

# Function to assign grade
def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Display results
print("\n--- Student Report ---")

for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: Marks = {marks}, Grade = {grade}")

print("\nTopper:", topper, "with", top_marks, "marks")
print("Class Average:", round(average, 2))