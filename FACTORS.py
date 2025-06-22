num = int(input("enter the number:"))
#10

i = 1
j = 0
while i <= num:
    if num % i == 0: 
        print(i,'is a factor of',num)
        j+=1
 
    i += 1 
    
if j>2:
    print("Not a prime number.")

else:
    print("Number is prime.")


# the itteration i += 1 is to given inside the while loop and not inside the if loop 
# as after one loop ends, the itteration will increase the number and the loop is again started
    