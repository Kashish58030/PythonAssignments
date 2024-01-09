l1 = [1, 2, 3, 4, 5]
l2= []
for i in range(len(l1)):
    l2.append(l1[-i-1])
print(l2)