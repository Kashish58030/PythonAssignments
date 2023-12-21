# 5. Student Grade Classification:
#    - Write a Python program to check if a student's grade falls into different categories. 
# If the grade is greater than or equal to 90, print "A"; if it's between 80 and 89, print "B"; 
# if it's between 70 and 79, print "C"; if it's between 60 and 69, print "D"; otherwise, print "F."

marks= 76

if(marks>=90):
    print("Grade A")
    
elif(marks==89 or marks>=80):
    print("Grade B")

elif(marks==79 or marks>=70):
    print("Grade C")

elif(marks==69 or marks>=60):
    print("Grade D")

else:
    print("F")