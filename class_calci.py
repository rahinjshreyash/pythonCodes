class Calci :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self,add):
        add = self.num1 + self.num2
        print('the addition is',add)

    def sub(self,sub):
        sub = self.num1 - self.num2
        print('the substraction is',sub)    

    def mul(self,mul):
        mul = self.num1 * self.num2
        print('the multiplication is',mul)

    def div(self,div):
        div = self.num1 / self.num2
        print('the division is',div)

            
claculate = Calci(8,4)
print(claculate.add(1))
    
        