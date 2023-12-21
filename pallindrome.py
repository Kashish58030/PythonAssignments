num=121
t1=num
rev=0
while(t1>0):
    digit=t1%10 
    rev=rev*10+digit
    t1//=10
    
if(rev==num):
    print("The number is a palindorme")
else:
    print("The number is not a palindrome")
    
    # write a program to print if a  given string is pallindrome or not

x="malayalam"

i=0
j=len(x)-1
check= True

while(i<j):
    if x[i]!=x[j]:
        check=False
    i+=1
    j-=1
if(check==True):
    print("It's a Pallindrome")
else:
    print("Not a Pallindrome")


     