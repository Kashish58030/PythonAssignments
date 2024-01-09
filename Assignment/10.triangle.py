# 10. Triangle Classification:
#     - Develop a Python program to classify a given triangle based on its sides. 
# If all three sides are equal, print "Equilateral"; if exactly two sides are equal, print "Isosceles";
# if all three sides are different, print "Scalene."

# Sides
a=5
b=66
c=6

if(a==b and b==c):
    print("Equilateral")
    
elif(a==b or b==c or c==a):
    print("Isosceles")

else:
    print("Scalene")