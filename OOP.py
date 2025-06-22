# OBJECT ORIENTED PROGRAMMING(OOP) is a programming paradigm which has a class c0ntaining objects which can have various attributes

# Objects are like humans, they have knowledge present in a memory location and they can  be remembered

class car(): # this is creating a class which is named as car
    pass

# adding object like honda , swift , tata to the class
honda = car()
tata = car()
swift = car()

# adding attributes to the objects
honda.weight = '1500'
honda.cng    = '50'
honda.petrol = '25'

swift.weight = '1700'
swift.cng = '30'
swift.petrol = '50'

# finally printing the attributes of objects given in a class
print('honda weight',honda.weight)
print(swift.__dict__)


# THE __init__ METHOD :
'''The __init__ method in a class is like creating a class in which attributes are defined and can be intialized to any object'''

# create a class by __init_ method
class Div_B :
    def __init__(self,address,percentage,hobby):
        
        self.address = address
        self.percentage = percentage
        self.hobby = hobby

shreyash = Div_B('pune','7.9','cricket')
praphull = Div_B('bihar','8.36','chess')
samruddhi = Div_B('sangamner','8.36','dance')

print(praphull.__dict__)
print('There are few children in Division B.Shreyash is one of the student who lives in',shreyash.address,'he got a total percentage of',shreyash.percentage,'in 1st sem.He also has intrest in',shreyash.hobby,'allover is a very good student')

# METHODS IN CLASS :

# 1. speak method - 
class person :
    def __init__(self,name,age,country,height,max_speed):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
        self.max_speed = max_speed
        self.speed = 0
       
    def speak(self):
        print('Hello my name is',self.name,'i am',self.age,'years old.I live in my country',self.country,'and my height is',self.height,'i can run at a speed of',self.speed)  
# 2. greet method -
    def greet(self,person):
        if person.name == 'maaz':
            print('hello neighbour!')
        else :
            print('hello',person.name)

# 3. accelerate method -
    def accelerate(self,add_speed):
        self.speed += add_speed
        if self.speed > self.max_speed :
            self.speed = self.max_speed      
# the atrributes are given all together ...
Name = person('shreyash','19','INDIA','155 cm',40)
Name2 =person('maaz','18','INDIA','156 cm',37)  
Name.speak()
Name.greet(Name2)
for i in range (0,1):
    Name.accelerate(20)
    Name.accelerate(40)
print(Name.__dict__)

# Class attributes :

class Web ():
    connected = True
    

    def __init__(self,page):
        pass
        self.history = [page]
        self.current = page
        self.incognito = False
        
     
    def navigate(self,new_page):
        self.current = new_page
        self.incognito = False
        if not self.incognito:
            self.history.append(new_page)

    def clear_history(self):
        self.history[:-1] = []    

    @classmethod
    def with_incognito(cls,page):
        instance = cls(page)
        instance.incognito = True 
        instance.history = []       
        return instance

edge = Web.with_incognito('instagram')
print(edge.__dict__)

opera = Web('snapchat')
print(opera.__dict__)


