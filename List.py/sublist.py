my_list = [1, 2, 3, 4, 5, 6, 7, 8,9]
sub_list_size = 3
result = []
temp = []
for i in my_list:
    temp.append(i)
    if len(temp) == sub_list_size:
        result.append(temp)
        temp = []
if temp:
    result.append(temp)

print(result)