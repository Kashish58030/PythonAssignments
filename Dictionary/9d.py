# Sort a dictionary by values in ascending order. Print the sorted dictionary
d = {"A": "Apple" , "C ": "Car ", "H" : "Height", "B" : "Ball"}
l = []
for i,j in d.items():
    l.append((i,j))
l.sort()
print(l)