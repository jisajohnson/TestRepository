#1. Greet a user

def greet_user(name):
    """Greets the user with their name."""
    return f"Hello, {name}! Welcome to Python programming."
print(greet_user("Jisa"))

#2. Add two numbers

def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 +num2
print(add_numbers(5,10))

#3. Check even or odd

def check_even_odd(number):
    """Checks if a number is even or odd."""
    return "Even" if number%2==0 else "Odd"

print(check_even_odd(7))
print(check_even_odd(8))
#print(check_even_odd(int(input("Enter a number:"))))

#4. Find the Largest Number

def find_largest(num1, num2, num3):
    """Finds and returns the largest of three numbers."""
    return max(num1,num2,num3)
print(find_largest(10,20,15))

#5. Calculate factorial
def calculate_factorial(n):
    """Calculates the factorial of a number."""
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
print(calculate_factorial(5))

#6.Reverse a String
def reverse_string(text):
    """Reverses the input string."""
    return text[::-1]
print(reverse_string("Python"))

#7. Check Prime Number
def is_prime(number):
    """Check if a number is prime."""
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))

#8. Count Vowels in a String
def count_vowels(text):
    """Counts the number of vowels in the input string."""
    vowels ="aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("I love Python programming"))

#9. Find the Maximum in a List
def find_max_in_list(numbers):
    """Finds the maximum number in a list."""
    return max(numbers)
print(find_max_in_list([3,5,2,9,1]))

#10. Convert Temperature
def convert_temperature(temperature,scale):
    """Convert temperature between Celsius and Fahrenheit."""
    if scale=="C":
        return(temperature*9/5)+32
    elif scale=="F":
        return(temperature-32)*5/9
    else:
        return "Invalid scale"
print(convert_temperature(0,"C"))
print(convert_temperature(32,"F"))

#11. Finding average of 4 different variables
def find_average(subject1,subject2,subject3,subject4):
    """Find the average of 4 subjects"""
    return (subject1+subject2+subject3+subject4)/4

subject1 = float(input("Enter the marks for subject 1: "))
subject2 = float(input("Enter the marks for subject 2: "))
subject3 = float(input("Enter the marks for subject 3: "))
subject4 = float(input("Enter the marks for subject 4: "))

print(find_average(subject1,subject2,subject3,subject4))

