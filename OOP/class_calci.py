class Calci :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        a = self.num1 + self.num2
        print('the addition is',a)

    def sub(self):
        s = self.num1 - self.num2
        print('the substraction is',s)

    def mul(self):
        m = self.num1 * self.num2
        print('the multipication is',m)

    def div(self):
        d = self.num1/self.num2
        print('the division is',d)

calculator = Calci(8,4)
calculator.sub()

calculator.div()






    
        