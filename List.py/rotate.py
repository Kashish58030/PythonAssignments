my_list = [1, 2, 3, 4, 5]
rotate_by = 2 
c=my_list.reverse()
print(my_list)
my_list[0]
# Given list
my_list = [1, 2, 3, 4, 5]

# Rotate by 2 positions
for i in range(2):
    temp = my_list[0]
    for i in range(len(my_list)-1):
        my_list[i] = my_list[i+1]
    my_list[-1] = temp

print(my_list)

# Given list
my_list = [1, 2, 3, 4, 5]

# Rotate by 2 positions
for _ in range(2):
    last_element = my_list.pop()
    my_list.insert(0, last_element)

print(my_list)