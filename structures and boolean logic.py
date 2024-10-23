#Basic If else Examples

## 1. Basic 'if-else' Example
age = int(input("Enter your age:"))

if age >= 18:
    print ("You are an adult.")
else:
    print ("You are not an adult.")

#2. 'if-elif-else' Example

marks = int(input('Enter your marks:'))

if marks >= 90:
    print("Grade:A")
elif marks >= 75:
    print("Grade:B")
elif marks >= 60:
    print("Grade:C")
else:
    print("Grade:F")

#3. Multiple Conditions with 'and' and 'or'
num= int(input('Enter a number:'))

if num > 0 and num < 10:
    print("The number is single-digit positive number.")
else:
    print("The number is either negative or has more than one digit.")

#4. Checking Even or Odd

number = int(input("Enter a number:"))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number.")

##5. Nested 'if-else'

number= int(input("Enter a number:"))

if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")