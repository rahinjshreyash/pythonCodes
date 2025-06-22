# DICTIONARY 
# 1ST WAY TO CREATE DICTIONARY:
nicknames = {'shreyash':'shree','praphull':'praf','samruddhi':'sam'}
print(nicknames['samruddhi'])
print(nicknames)

# 2ND WAY:
trophies = dict(rcb =0,mi=5,kkr=3,csk=5)
print(trophies)
print(trophies['rcb'])

# DICTIONARY METHODS:

# 1. dict.copy()
ipl = trophies.copy()
print(ipl)

# 2. dict.update()
trophies.update({'dc':1})
print(trophies)

# 3. dict.keys()
print(trophies.keys())

# 4. dict.fromkeys()
my_friends = ['praphull','maaz','rupali']
names =dict.fromkeys(my_friends)
print(names)

# 5. dict.get(key)
print(trophies.get('csk'))

# 6. max(dict)
print(max(trophies))

# 7. min(dict)
print(min(trophies))

# 8. dict.pop()
numbers = {'a':1, 'b':2,'c':3,'d':4}
print(numbers.pop('b'))
print(numbers)

# 9. dict.popitem
print(numbers.popitem())
print(numbers)

# 10. dict.clear()
trophies.clear()  # will clear the dictionary named trophies

# ITERATION IN DICTIONARY
runs = {
    'rohit': 256,
    'virat': 85,
    'dhoni': 91,
    'gambhir': 97,
    'shreyas': 65
}
for name in runs:
    print(name ,'has scored',runs[name],'in important match')
    # in this code , the name variable is been defined as a key,so as we print name, key will be the output, now when we search name inside the dictionary, i.e runs[name]
    # then the name is been defined as value,hence value will get printed in output.

letter = """hey dear, i just want to say this from so long that you look gorgeous. i really like whatever you do. I worship the floor where your steps fall. you are so beautiful that 
even in class, i can't get my eyes away from you. the way you listen, the way so speak, i like it so much. actually i am a bit shy and scared to tell you alll this, so i
wrote this letter for you. i want to spend more time with you, listening to stories, or chilling. i just want to conclude that i have a crush o you, and always wanted to
share my feelings with you. I hope you understand my feelings. thank you """

def text(letter):
    solution = {}
    for s in letter:
        s = s.lower()
        if s is not ' ':
            if s in solution:
                solution[s] += 1
            else:
                solution[s] = 1
    return solution

print(text(letter))

# THE in keyword !!!
print('sachin' in runs)
print('rohit' in runs)

# ORDERED DICTIONARIES KI MKC :)

from collections import OrderedDict
a = OrderedDict() 
print(a)





              