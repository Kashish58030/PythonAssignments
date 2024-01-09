# Age Group Classification:
#    - Write a Python program using the `match` statement to classify a person's age group.
# If the age is less than 18, print "Under 18"; if it's between 18 and 35 (inclusive), print "18-35"; 
# if it's between 36 and 60 (inclusive), print "36-60"; otherwise, print "Over 60."

age=int(input("Enter the age:"))

match age:
    case _ if age<18:
        print("under age")
        
    case _ if age>=18 and age <=35:
        print("18-35")
        
    case _ if age>=36 and age<=60:
        print("36-60")
   
    case _:
        print("Over 60")
