import random

def data() :
   possible = []
   output = []

   price = 0.10

   while price <= 1.45 :
    price += 0.01

    possible.append(round(price,2))
  
   for i in range (0,30):
      
      output.append(random.choice(possible))

   return output

print(data())
 