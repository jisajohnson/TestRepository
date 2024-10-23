totalamount = int(input("Enter the total bill amount:"))
discount = 0.1

if totalamount > 50:
    if discount:
        print("New total with discount",totalamount+totalamount*discount)
else:
    print("Total amount:", totalamount)

age = int(input("Enter your age:"))

if age <= 12:
    print ("The ticket price is £5")
elif age <= 17:
    print ("The ticket price is £7")
elif age <= 64:
    print ("The ticket price is £10")
else:
    print ("The ticket price is £6")

amount = float(input("Enter the withdrawal amount:"))

if amount >= 1000:
    print("Thank you for being our special customer and Please come again. The amount you have withdrawn",amount)
elif amount <= 100:
    print("WARNING: You have insufficient balance")
else:
    print ("The amount for withdrawal:",amount)