
# 12. Time of the Day:
#     - Create a Python program to determine the time of the day based on the given hour. 
# If the hour is between 5 AM and 11 AM, print "Good Morning"; if it's between 12 PM and 4 PM,
# print "Good Afternoon"; if it's between 5 PM and 8 PM, print "Good Evening"; otherwise, print "Good Night."

Hour= 1

if(Hour>=5 and Hour<="11Am" ):
    print("Good Morning")

elif(Hour>=12 and Hour <=16):
    print("Good Afternoon")

elif(Hour>=17 and Hour<=20):
    print("Good Evening")

else:
    print("Good Night")