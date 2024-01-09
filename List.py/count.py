# Write code that counts how many times each unique element appears in a list.
# Example: Input ["apple", "banana", "apple", "cherry", "banana"] should output apple: 2, banana: 2, cherry: 1.

l=["apple","banana","apple","cherry","banana","mango"]
b=set({})
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    b.add((l[i],count))
print(b)
        