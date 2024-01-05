# 5. Add a new contact to a dictionary of friends. Print the updated dictionary.
f_d={"Aarav":250,"Subham":236,"Abhishek":256}
l = []
for i,j in f_d.items():
    l.append((i,j))
l.append(("Kashish", 243))
print(dict(l))