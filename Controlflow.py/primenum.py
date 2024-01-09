# Check if a number is a prime number

num = 37
x = True

for i in range(2,num):
    # 6%2==0
    if(num%i==0):
        x = False
        break

if(x==True):
    print("Prime Number")
else:
    print("Not Prime")
