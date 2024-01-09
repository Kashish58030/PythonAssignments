# 8. Palindrome Check:
#    - Create a Python program to check if a given string is a palindrome. 
# If the string is a palindrome (reads the same backward as forward), print "Palindrome"; otherwise, print "Not a palindrome."

W= input("Enter a word: ")

i=0
j=len(W)-1
Check=True
while i<j:
    if W[i]!=W[j]:
        Check=False
    i+=1
    j-=1
if Check==True:
    print("It's a pallindrome")
else:
    print("It's not a pallindrome")
