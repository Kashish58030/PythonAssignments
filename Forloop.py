# initialize,condition,skip
# start,stop,skip

# 1.print 1 to 10
# for i in range(1,11):
#     print(i)

# 2.print 10to 1
 

# 3. print the sum of all numbers from 1 to 10
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

# 4.print product of all numbers from 1 to 10
product=1
for i in range(1,6):
    product*=i
print(product)

# 5.print all the even numbers between 1 to 100

# for i in range(1,101):
#     if i%2==0:
#         print(i)

# 6.count all the even numbers between 21 to 78

# count=0
# for i in range(21,79):
#     if i%2==0:
#         count+=1
# print(count)

# count all the even numbers between  1 to 10
# count=0
# for i in range(1,11):
#     if i%2==0:
#         count+=1
# print(count)

# sum all the even numbers
# sum =0
# for i in range (1,101):
#     if i%2==0:
#         sum +=i
# print(sum)

# Check if a number is a prime number

# num = 37
# x = True

# for i in range(2,num):
#     # 6%2==0
#     if(num%i==0):
#         x = False
#         break

# if(x==True):
#     print("Prime Number")
# else:
#     print("Not Prime")

 
   
# #  18Dec
# # armstrong number
# num=1634
# #   count the number of digits
# digit=0
# t1=num
# while(t1>0):
#     t1//=10
#     digit+=1
# # multiply individual digit to the number of total digits
# t2=num
# sum=0
# while(t2>0):
#     rem=t2%10
#     product=1
#     for i in range(1,digit+1):
#         product*=rem
#     #  add the products
#     sum+=product
#     t2//=10 
    

# # compare the sum to the original number
# if(num==sum):
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
