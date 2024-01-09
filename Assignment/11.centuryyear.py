# 11. Century Year Check:
#     - Create a Python program to determine if a given year is a century year or not. 
# If the year is a century year (ends with '00'), print "Century year"; otherwise, print "Not a century year."

year=2100

if(year%100==0):
    print("It's a Century Year")
    
else:
    print("Not a Century Year")