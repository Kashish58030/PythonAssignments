# Create two dictionaries representing contacts. Merge them and print the combined dictionary.
a={"Aman":9753565653,"John":9835654454}
b={"Kriya":9770253241," neha":9421124364}
c=[]
for i,j in a.items():
    c.append((i,j))
for m,n in b.items():
    c.append((m,n))
print(dict(c))
    