#   SETS
'''Sets are almost same like thr lists, the differencr between sets and lists is that each element in sets should be unique which is unlike the lists
let's try once'''
lists = [1,1,1,3,4,4]
sets= {1,1,1,3,4,4}
print(lists)
print(sets)

'''when you run this code you will find that lists can run an element multiple times, but in sets the elements are not printed multiple times'''

# SET METHODS
sets.add(9)
print(sets) # in this code an element can be added in the set
num = {5,6,7,8}

sets.update(num) # in this code , another sets can be added in a single set
print(sets)

'''we can also remove elements from sets, there are three methods'''
# 1. 
sets.remove(9)
print(sets)# this will remove an element in the set

# 2.
sets.discard(3)
print(sets) # discard will remove that element forever from the set....like if added another samr element...it will not get printed

# 3. 
print(sets.pop())# it will just remove the input element and print the element which is removed
print(sets)


# SOME RELATIONS BETWEEN TEO SETS
 # 1. set.union()
a = {7,8,1,2,3,9,4,5,6}
b = {4,5,6}
print(a.union(b))
'''if you have studied maths in 9th class 1st chapter sets, you will know that union os two sets is the combination of the two sets, this code can also be wrriten in boolean form using |  '''
# NOTE : SET HAS A PROPERTY THAT SET WILL ALWAYS PRINT THE ELEMENTS IN ASCENDING ORDER

# 2. set.intersection()
print(a.intersection(b))
''' intersection of two sets means the common elements present in both sets , this can also be done in boolean form using &'''

# 3. set.difference()
print(a.difference(b))
'''the difference of sets will print the elements which are present in one set, but not in the other set'''

# 4. set.symetric_difference()
print(a.symmetric_difference(b))
'''using symetric_difference , we can also print those elements which are not common in both the sets'''

# 5. set.issubset()
print(b.issubset(a))
''' subset means all the elements present in one set are also present in the other subset or not, if they are present then output is true else false'''

# 6. set.superset()
print(a.issuperset(b))
'''if b is subset of a then automatically a is superset of b'''
