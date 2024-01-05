# 6. Remove a specific key-value pair from a dictionary of countries and capitals. Print the modified dictionary.

c={"India":"Delhi","UK":"London"}
l = []
for i in c.items():
    l.append(i)
print(l)
l.pop()
print(dict(l))