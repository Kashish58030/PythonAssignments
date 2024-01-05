# Given a list of ages, filter out the adults (age >= 18). Print the modified list.
Age=[20,18,36,15,13,7,9]
mod=[]
for i in range(len(Age)):
    if Age[i]>=18:
        mod.append(Age[i])
print(mod)  
print()