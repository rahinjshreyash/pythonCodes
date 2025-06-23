# NAME PLATE USING DEFINE FUNCTION
def name_plate(name, length,symbol):
    print(symbol*length) # This line will give the upper frame by printing given symbols for given length
    print(symbol*2 + (length-4)*'-' + symbol*2) #this will construct the frame by just creatin 2 symbols at start and end as given in equation
    print(symbol*2 + name.center(length-4,'-')+symbol*2) # name.center is used to adjust your name in the center of the frame
    print(symbol*2 + (length-4)*'-' + symbol*2)
    print(symbol*length)

name_plate('SHREYASH',30,'*')

# EXAMPLE ON ANONYMAS OR LAMBDA FUNCTION
kinetic_energy = lambda m,v : (m* v**2)/2 
print('the kinetic energy is',kinetic_energy(12,5),'joules')