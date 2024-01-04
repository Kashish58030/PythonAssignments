# Given a set of even numbers, filter out the multiples of 4. Print the modified set.
even_num={2,4,6,8,10,12,14,16,18,20}
m_set={i for i in even_num if i% 4!=0}
print(m_set)
