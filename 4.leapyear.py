# # 4. Leap Year Check:
# #    - Create a Python program to determine if a given year is a leap year or not. If the year is a leap year, print "Leap year"; 
# #    otherwise, print "Not a leap year."


# year=1900

# if(year%4==0):
#     print("It's a leap year")
    
# else:
#     print("It's not a leap year")

year = 2012
# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{ a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(" not a leap year".format(year))