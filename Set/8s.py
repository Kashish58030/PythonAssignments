#  Generate a set of cubes for numbers 1 to 5 using set comprehension. Print the resulting set.
n={1,2,3,4,5}
cubes={x**3 for x in n}
print(cubes)