# armstrong number
num=370   
#   count the number of digits
digit=0
t1=num
while(t1>0):
    t1//=10
    digit+=1
# multiply individual digit to the number of total digits
t2=num
sum=0
while(t2>0):
    rem=t2%10
    product=1

    for i in range(1,digit+1): 
        product*=rem
    #  add the products
    sum+=product
    t2//=10 
    

# compare the sum to the original number
if(num==sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
 