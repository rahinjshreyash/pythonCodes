import random 
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's',  't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_and_digits = ['1','2','3','4','5','6','7','8','9','0','@','#','$','_','-']

def generate(list, size):
    generated_op = []
    
    for i in range(size):
        char = random.choice(list)
        generated_op.append(char)
    return generated_op
        


length = int(input("Length of the password: "))
def password_generator(length):
    password = "".join((generate(alphabets,int(length))))
    print(password)

password_generator(length)
