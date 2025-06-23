temp=[32, 28 ,40 ,29, 35,27]
location = 'india'

def temperature(value):
    day = 1
    for v in value:
         print('temeratue at', location,'on day', day,':', v)
         day += 1
        
def average(value):
     import math
     average = math.fsum(value)/ len(value)
     print('the average temperature at',location, 'is',average)

average(temp)
print(len(temp))