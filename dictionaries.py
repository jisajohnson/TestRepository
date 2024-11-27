#1. Introduction to Dictionaries
student={"name":"Alice",
         "age":20,
         "courses":["Math","Physics"]} #Creating Dictionary
print(student)

items={"Title":"Bag",
       "price":"$200",
       "quantity":25}
print(items)

#2. Creating Dictionaries
student_info={
    "name":"Bob",
    "age":21,
    "major":"Computer Science"
} #Creating a dictionary 
print(student_info)

#Using dict function
student_info2=dict(name="Emma",age=22,major="Biology") #Creating dictonary using the dict function
print(student_info2)

#3. Accessing Dictionary Elements
student={
    "name":"Charlie",
    "age":19,
    "major":"Physics"
}
#Accessing  using key
print(student["name"])

#Using .get() to access key safely
print(student.get("GPA","Not Available"))

#4. Modifying Dictionary ELements
student={
    "name":"Dave",
    "age":20,
    "major":"Chemistry"
}

#Adding a new key-value pair
student["GPA"]=3.8
print(student)

#Modifying an existing key-value pair
student["age"]=21
print(student)

#Removing a key-value pair
student.pop("major")
print(student)

#5. Dictionary Methods and Operations

student={
    "name":"Eve",
    "age":22,
    "major":"Biology"
}

#Using .keys(), .values() and .items()
print(student.keys())
print(student.values())
print(student.items())

#Looping through a dictionary
for key, value in student.items():
    print(f"{key}:{value}")

#Check if a key exists
if "GPA" in student:
    print("GPA is:", student["GPA"])
else:
    print("GPA key not found")

#6. Nesting Dictionaries
school={
    "Student1":{"name":"ALice","age":20,"GPA":3.9},
    "Student2":{"name":"Bob","age":21,"GPA":3.6}
    }
 #Accessing nested dictionary values
 



