# 6. Largest of Three Numbers:
#    - Develop a Python program to determine the largest of three numbers.
# If the first number is the largest, print "First number is the largest"; 
# if the second number is the largest, print "Second number is the largest";
# if the third number is the largest, print "Third number is the largest."

First_Num=94
Second_Num=36
Third_Num=94

if(First_Num>Second_Num and First_Num>Third_Num):
    print("First Number is the largest")
    
elif(Second_Num>First_Num and Second_Num>Third_Num):
    print("Second Number is the largest")
    
elif(Third_Num>First_Num and Third_Num>Second_Num):
    print("Third Number is the largest")
    
else:
    print("Two Numbers are equal or All numbers are equal")