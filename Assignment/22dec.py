# # #  Write a program to convert Celsius to Fahrenheit.
# # n = 5
# # # for i in range(n):
# # #     print(' ' * (n - i - 1) + '*' * (2* i + 1))


# # for i in range(n, 0, -1):
# #     print(' ' * (n - i) + '*' * (2 * i + 1))

# num_students = int(input("Enter the number of students: "))
# student_info = []
# for _ in range(num_students):
#     name = input("Enter student name: ")
#     age = int(input("Enter student age: "))
#     student_info.append((name, age))

# total_age = sum(age for i, age in student_info)
# average_age = total_age / len(student_info)
# print(average_age)

# Define a tuple with details of a book
book_details = ("Python Programming", "John Doe", 2022)

# Unpack the tuple into separate variables and print them
title, author, year = book_details
print("Title:", title)
print("Author:", author)
print("Year:", year)