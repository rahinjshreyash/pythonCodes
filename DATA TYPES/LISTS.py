# LISTS

# addition of lists
my_friends = ['praphull','maaz','rohan']
your_friends = ['shreyash','rupali','mayuri','ariba']

print(my_friends + your_friends )
           # or
my_friends += your_friends
print(my_friends)

# selcting an element in lists
print(my_friends[4])

# replacing an element 
my_friends[4] = 'samruddhi'
print(my_friends)

# LIST FUNCTIONS

# 1. no. of elements in the string[ len function ]
print(len(my_friends))

# 2. to find max number or biggest alphabet [max function]
print(max(my_friends))

# 3. to find min number or lowest alphabet [min function]
print(min(my_friends))

# 4. to find sum [sum function]
numbers = [4,5,6,7]
print(sum(numbers))
average = sum(numbers)/4
print('average is',average)


# 5. sort alphabetically or in increasing order [sorted function]
print(sorted(my_friends))



# NESTED LIST (LIST INSIDE A LIST!!!)

list1 = [1 , 2 , 3 ,4 ,5, 6 , 7, 8 ,9 , [10,11,12,13]]

print(list1[5])
print(list1[9][3])

list1[9][2] = 14
print(list1[9])

# LIST FUNCTIONS....
# 1. list.append() :

my_friends.append('kashaf')
print(my_friends)

# 2. list.extend() :
my_friends.extend(list1)
print(my_friends)

# 3. list.insert([],) :
my_friends.insert(5,'divya')
print(my_friends)

# 4. list.remove() :
my_friends.remove('rohan')
print(my_friends)

# 5. list.pop() :
my_friends.pop()
print(my_friends)

# 6. list.index()
print(my_friends.index('samruddhi'))

# 7. list.count(item)
print(my_friends.count('samruddhi'))

# 8. list.reverse()
my_friends.reverse()
print(my_friends)

# 9. list.copy()
my_friends.copy()
print(my_friends)

# 10. list.sort()
your_friends.sort()
print(your_friends)

# 11. list.clear() 
print(my_friends.clear())


   