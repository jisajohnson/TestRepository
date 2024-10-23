#1. Restaurant Order Discount
totalamount = int(input("Enter the total bill amount:"))
discount = 0.1

if totalamount > 50:
    if discount:
        print("New total with discount",totalamount+totalamount*discount)
else:
    print("Total amount:", totalamount)

#2. Movie Ticket Price
age = int(input("Enter your age:"))

if age <= 12:
    print ("The ticket price is £5")
elif age <= 17:
    print ("The ticket price is £7")
elif age <= 64:
    print ("The ticket price is £10")
else:
    print ("The ticket price is £6")

#3. Bank Withdrawal
amount = float(input("Enter the withdrawal amount:"))

if amount >= 1000:
    print("Thank you for being our special customer and You will be upgraded to VIP. The amount you have withdrawn is £",amount)
elif amount <= 100:
    print("WARNING: You have insufficient balance")
else:
    print ("The amount for withdrawal: £",amount)

#4. Weather and Outfit Selection
weather = int(input("Enter the weather:"))
rainy = input("Is it raining?(Yes/No)")
cloudy = input("Is it cloudy?(Yes/No)")
if weather > 25:
    print ("Wear shorts and sunglasses")
elif rainy == "Yes":
    print ("Carry an ummbrella")
elif weather < 10:
    print ("Wear a jacket")
elif cloudy == "Yes":
    print ("Wear light clothes")
else:
    print ("Wear casuals")

#5. Password Validation
username = "SystemOS"
password = str(input("Enter the password:"))
print(username)
if len(password) > 8 and len(password) < 16:
    if password == str and password == int:
        print("This Password is valid")
elif password < 8:
    print ("Minimun 8 characters")
elif password > 16:
    print ("Maximum 16 characters")
elif password != int:
    print ("At least one number")
elif password != str:
    print ("At least one character")
else:            
    print ("Error! The password isn't valid")
    print ("Minimun 8 characters")
    print ("Maximum 16 characters")
    print ("At least one number")
    print ("At least one character")
