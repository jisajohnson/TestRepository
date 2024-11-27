#1. Print Numbers from 1 to 10
for i in range (0,11):
    print(i)

#2. Sum of First 5 numbers
total = 0
for i in range(1,6):
    total +=i
    print("Sum:",total)

#3. Print each character in a string
text=input("Enter a string:")
for char in text:
    print(char)

#4. Count down from a Given Number
number=int(input("Enter a number:"))
while number >= 0:
    print(number)
    number -=1

#5.Multiplication
num= int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

#6.Sum of Elements in a List:-
numbers =[3,5,7,9,11]
total=0
for num in numbers:
    total += num
print("Sum of list elements:",total)

#7. Find minimum in a List
numbers=[12,4,56,17,8]
minimum= numbers[0]
for num in numbers:
    if num<minimum:
        minimum=num
print("Minimum value:", minimum)

#8. Guess the number
import random
target = random.randint(1,50)
guess = None
while guess != target:
    guess= int(input("Guess a number between 1 and 50:"))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print("Correct! You guessed the number.")

#9. Check for Prime Numbers
num=int(input("Enter a number:"))
is_prime=True
if num <=1:
    is_prime=False
else:
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            is_prime=False
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

