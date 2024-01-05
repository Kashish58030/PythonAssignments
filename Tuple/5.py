# Write a function that takes a tuple of student names and their ages. Return the average age.
num_students = int(input("Enter the number of students: "))
student_info = []
for _ in range(num_students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_info.append((name, age))

total_age = sum(age for i, age in student_info)
average_age = total_age / len(student_info)
print(average_age)
