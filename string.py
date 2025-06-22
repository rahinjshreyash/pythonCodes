# STRINGS

a = ('GOOD')
b = ('MORNING')
c = ('SIR')

#ADDITION
message = (a +' '+ b +' '+ c)
message += '!'
print(message)
print(message[5])# TO PRINT SINGLE ELEMENT IN STRING

# RANGE FOR STRINGS
print(message[0:5])
print(message[-5:-1])
print(message[3:])
print(message[:7])

# STRING INTERPOLATION METHODS
# 1. COMMAS
human =('shreyash')
pet  = ('parrot')
name = ('macow')

print(human , 'has a pet',pet, 'and his name is',name)

# 2. f'' format
print(f'{human} has a pet {pet} and his name is {name}')

# 3. str.format
print('{} has a pet {} and his name is {}'.format(human,pet,name))

# 4. % sign
print('%s has a pet %s and his name is %s' %(human,pet,name))

# STRING FUNCTIONS

# 1. str.capitalize()
print('SHREYASH IS A GENIUS'.capitalize())

# 2. str.lower()
print('SHREYASH IS A GENIUS'.lower())

# 3. str.upper()
print('shreyash is a genius'.upper())

# 4. str.startswith()
print('shreyash is a genius'.startswith('sh'))

# 5. str.endswith()
print('shreyash is a genius'.endswith('s'))

# 6. str.strip()
print('shreyash is a genius'.strip('s'))

# 7. str.replace()
print('shreyash is your teacher'.replace('teacher' , 'daddy'))

# 8. str.split()
print('shreyash is a genius'.split())

# 9. str.count()
print('shreyash is a genius'.count('s'))