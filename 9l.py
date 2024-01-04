#  Write a function that takes a list of numbers as input and returns the sum of the squares of each number.
l=[1,2,3,4,5,6]
s=0
for i in l:
    p=1
    p=i**2
    s+=p
print(s)