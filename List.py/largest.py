# numbers_list = [4, 7, 2, 9, 1, 5]

# if not numbers_list:
#     print("List is empty.")
# else:
#     largest_value = smallest_value = numbers_list[0]

#     for num in numbers_list:
#         if num > largest_value:
#             largest_value = num
#         elif num < smallest_value:
#             smallest_value = num

#     print("List:", numbers_list)
#     print("Largest Value:", largest_value)
#     print("Smallest Value:", smallest_value)
n=[37,40,66,75,10]
x=len(n)
for i in range(x):
    for j in range(0,x-i-1):
         if n[j]>n[j+1]:
             n[j],n[j+1]=n[j+1],n[j]
print(n[x-1])
print(n[0])