# TUPLE !!!!

my_friends = ('praphull','maaz','priya','rupali','divya','samruddhi','rohan','ariba','kashaf','sumit','ruchila','shivam',1,2,3.14,6)

print(my_friends)

# AN ELEMENT IN TUPLE
print(my_friends[5])

# PACKING TUPLE

file = 9, 2 ,'space'
print(file)

# UNPACKING TUPLE
a , b , c = file
print(a)
print(a,b,c)

# 2D TUPLE
letters = (('a','g'),('b','h'),('d','s'))
print(letters[2][1])

# SLICING TUPLE
print(my_friends[:6])

numbers = (1,2,3,4,5,6,7,8,9)
even_num = (numbers[1::2])
print(even_num)
odd_num = (numbers[::2])
print(odd_num)

# ITERATION WITH TUPLES :
if  len(numbers)<20:
    s = 1
    for some in numbers :
        print(numbers , s , )
        s +=1


# FUNCTIONS WITH TUPLES :

# 1. tuple.count()
print(numbers.count(1))

# 2. min()
print(min(numbers))

# 3. max()
print(max(numbers))

# 4. len()
print(len(my_friends))




    