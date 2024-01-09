# Day of the Week:
#    - Create a Python program using the `match` statement to identify the day of the week based on the numeric day.
# If the day is 1, print "Monday"; if it's 2, print "Tuesday"; and so on until 7 for "Sunday."

day =1

match day:
    case 1:
        print("Monnday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")