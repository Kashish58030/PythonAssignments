# 14. Ticket Price Calculation:
#     - Develop a Python program to calculate the ticket price based on the age of the person.
# If the age is less than 12, the ticket price is $5; if the age is between 12 and 18 (inclusive), 
# the ticket price is $10; if the age is 65 or older, the ticket price is $8; otherwise, the ticket price is $15.

age=66

if(age<12):
    print("The ticket price is $5")

elif(age>=12 and age<18):
    print("The ticket price is $10")

elif(age>=65):
    print("The ticket price is $8")

else:
    print("The ticket price is $15")