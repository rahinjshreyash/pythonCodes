# USER INPUT

print('hello...what is your name?')
name = input()
print('hello' , name , 'what is your age?')
age = int(input())
print('so next year you will be', age+1)

# DAYS TO YEARS CONVERTER

print('enter the number of days')
days = int(input())

years = days // 365
print( 'the number of years covered are',years)

# FOR WEEKS
weeks = (days % 365)// 7
print('the no of weeks are',weeks)

# FOR REMAINING DAYS
remaining_days = (days) - (years*365) - (weeks*7)
print('the remaning days are equal to', remaining_days)

# BINARY OCTAL AND HEXA
num = int(input('ENTER THE NUMBER:'))

print(bin(num))
print(hex(num))
print(oct(num))

# DC 14 3C HEXADECIMAL

r = int('DC',16)
g = int('14',16)
b = int('3C',16)

print(r,g,b)

