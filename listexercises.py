#1. Creating List
fruits = ["apple","banana","cherry","date"]
print(fruits) #prints the fruits in the list

#2. Access List Elements
numbers = [10,20,30,40,50]
print("First element:", numbers[0]) #prints the first element in the list
print("Last element:", numbers[-1]) #prints the last element in the list

#3. Updating List Element
animals = ["cat","dog","bird"]
animals[1]="hamster" #replacing the 2nd element with hamster
print(animals) #prints the new list

#4. Append and Remove Elements
colors = [] #created an empty list
print(colors)
colors.append("Red") #adds new elements in the list
colors.append("Blue") 
colors.append("Green")
print(colors)
colors.remove("Green") #removes the element in the list
print(colors)

#5. List length
names = ["Alice","Bob","Charlie","Diana"]
print("Length of the list:", len(names)) #gives the length of the list

#6. Sum of list elements
numbers = [4,7,1,8,5]
total_sum= sum(numbers) #used for getting the total sum
print("Sum of elements:", total_sum) #finds the sum of the numbers in the list

#7.Find Maximum and Minimum Elements
ages=[23,45,18,34,60]
print("Maximum age:", max(ages)) #prints the maximum age
print("Minimum ages:", min(ages)) #prints the minimum age in the list

#8. Sort a list
scores = [88,56,92,78,61]
scores.sort() #Sorts the list in ascending order(default)
print("Sorted list:",scores)

#9. Check if element exists in the list
numbers =[1,3,5,7,9]
if 5 in numbers:
    print("Found") #to check if 5 is there in the list
else:
    print("Not Found") #if 5 isn't there in the list, this will be the output

#10. Count Occurences of an element
items = [1,2,2,3,4,4,4,5]
count_of_4= items.count(4) #to check how many 4 are there in the list
print("Count of 4:",count_of_4) #print the number of 4 present in the list

#11. Extending and Reversing a list
list1=[2,4,6,8,10]
list2=[1,3,5]
list1.extend(list2) #to extent the list1 with list2
print(list1) #prints both the list together in one line
list1.reverse() #to reverse the list 
print(list1) #prints the reversed list
