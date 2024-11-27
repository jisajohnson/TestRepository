#1.Creating a tuple
fruits=("apple","banana","cherry") #Create a tuple 
print(fruits) #Print Fruits
print(type(fruits)) #finds the class type
#fruits[0]='orange'

#2. Accessing Elements
print(fruits[1]) #prints the second element
print(fruits[-1]) #prints the last first element

#3. Unpacking Tuples
colors=('red','green','blue') #Create a tuple 
color1, color2, color3= colors #combining all of them in one tuple
print(color1) #prints color1
print(color2) #prints color2
print(color3) #print color3

#4. Tuple Concatenation
numbers1=(1,2,3) #Create a tuple with numbers
numbers2=(4,5,6) #Create a tuple with numbers
numbers_combined=numbers1+numbers2 #Combines number1 and number2
print(numbers_combined) #prints the combines numbers

#5. Tuple Slicing 
alphabet=('a','b','c','d','e','f','g') #Create a tuple with different alphabets
print(alphabet[:3]) #Prints the first three elements
print(alphabet[-3:]) #Prints the last three elements
print(alphabet[::2]) #Prints the alternate elements

#6. Tuple Methods
numbers=(1,2,2,3,4,4,4,5) #Create a tuple of random numbers
print(numbers.count(4)) #Prints the count of 4
print(numbers.index(2)) #Prints the 

#7. Nested Tuples
nested=(1,2,(3,4),5) #Create a nested tuple
print(nested[2][1]) #prints the nested tuples

#8. Tuple Membership Testing
colors=('red','green','blue') #Create a tuple with colors
print('yellow' in colors) #Checks if there is the color "yellow" in the tuple
print('blue' in colors) #Checks if there is the color "blue" in the tuple 
