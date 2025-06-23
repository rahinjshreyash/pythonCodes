# In class methods...you must have observed that we can't print all attributs....like some attributes can change....and some cannot....these are protected attributes which cannot change..
class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.model = model
        self.__year = year

    def get__make(self): # we use these methods to obtian the protected attributes
        return self.__make
    
    def get__year(self):
        return self.__year

honda = Car('alter','5','2006')

print(honda.__dict__)  
print(honda.get__year())   

# CLASS INHERITANCE
# this means we can use class attribute to other classes

class Dog :
    def __init__(self,mass,life_span,speed):
        self.mass = mass
        self.life_span = life_span
        self.speed = speed

    def vocalize(self):
        print('bhawwwww')
    
    def __str__(self):
        return f'The {type(self).__name__.lower()} is an animal.' \
               f'It weighs on an average of {self.mass}kg.'\
               f'Tt has a life span of about {self.life_span}years.'\
               f'It can run at a speed of {self.speed}km/hr.'        
    # now we have created a class dog....we can use the same in other class like these

class Cat(Dog):
    def __init__(self,mass,life_span,speed,spotted):
        super().__init__(mass,life_span,speed)
        self.spotted = spotted
        st = spotted

        
    def vocalize(self):
        print('meoooowwwww')

    
    def __str__(self):
        if self.spotted == True:
           st = 'spotted'
        
        else:
            st = ''

        return f'The {st} {type(self).__name__.lower()} is an animal.' \
               f'It weighs on an average of {self.mass}kg.'\
               f'Tt has a life span of about {self.life_span}years.'\
               f'It can run at a speed of {self.speed}km/hr.'    
    
class horse(Dog):
    def vocalize(self):
        print('neiiiiiiiigh')   



kitty = Cat('13','20','34',True)
print(kitty)
kitty.vocalize()

tom = Dog('25','25','35')
print(tom)


# mix class (mixens):
class moblie :
    def __init__(self,memory):
        self.memory = memory

class camera :
    def take_pic(self):
        print('say cheese')

class smart(moblie,camera):
    pass

apple = smart('16GB')
print(apple.memory)
apple.take_pic()
        