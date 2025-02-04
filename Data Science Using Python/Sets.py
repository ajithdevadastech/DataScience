#Creating Sets
vowels = {'a','a', 'e', 'i', 'o', 'u'}
print('Set of vowels:',vowels)
set_a={0,8,6,3,2,1,4,6,4,8,0,1}
set_b={4,324,25,25,23,51,3}
print('Set A:',set_a)
print('Set B:',set_b)

# set difference
print('Elements in A but not in B',set_a-set_b)
print('Elements in B but not in A',set_b-set_a)

# Union and Intersection
print('Union of sets A and B:',set_a.union(set_b))
print('Intersection of A and B',set_a.intersection(set_b))

# Insertion and Update
set_a.add(5)
set_a.update([5,6,6])
print('Set A after inserting 5 and updating from a list:',set_a)

# Membership operator
print( 1 in set_a)
print(1 in set_b)

# Inbuilt functions will work on any type of iterable
print(all(set_a)<100) # returns true if every item in iterable is holds the condition
print(any(set_a)>10) # returns true if any one item in iterable holds the condition