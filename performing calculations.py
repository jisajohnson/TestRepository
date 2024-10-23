a= 20
b= 10
sum = a+b
print ("The sum of two number is",sum) #adding the numbers
difference = a-b
print ("The difference of two number is",difference) #subtracting the two numbers
multiply = a*b
print ("The multiplication of two numbers is",multiply) #multiply two numbers
divide = a/b
print ("The division of two numbers is",divide) #divide two numbers
floordivision = a//b
print ("The floor divison of two numbers is",floordivision) #to find the floor division of two numbers
modulus = a%b 
print ("The modulus of two numbers is",modulus) #to find the modulus 
exponentiation = a**b
print ("The exponentiation of two numbers is",exponentiation) #to find exponentiation

Monday = 1500
Tuesday = 2300
Wednesday = 700
print("Monday's sales are", Monday,
      "and Tuesday's sales are", Tuesday,
      "and Wednesday's sales are", Wednesday)
value1 = 12
value2 = 42
value3 = 3
value4 = 10
value5 = 7
value6 = 1
total = (value1 + value2 +
         value3 + value4 +
         value5 + value6)

message = 'Hello '+'World'
print (message)

print ('Enter the amount of ' + 
       'sales for each day and ' +
       'presss Enter.')

print (f'Hello World') #It's a formated string

name = 'Johnny'
print(f'Hello World {name}.') #formated sentence

print(f'The value is {10+2}.') 
val = 10
print(f'The value is {val+1}.') #formated expressions

num = 123.456789
print (f'{num:.2f}')

num = 1000000.00
print(f'{num:,.2f}')

discount = 0.5
print(f'{discount:.0%}') #formatted output with f-strings

num = 123456789
print(f'{num:,d}')

num = 12345.6789
print(f'{num:.2e}')

num = 12345.6789
print(f'The number is {num:12,.2f}') #specifying a minimum field width

print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}') #aligning values within a field

number = 12345.6789
print(f'{number:^10,.2f}')

#import turtle
#turtle.forward(100) #moves turtle forward
#turtle.mainloop() #you can try turtle.done() as well

#import turtle
#turtle.backward(100)
#turtle.done()

import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.done()

