class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name} - ${self.price}" 
class Snack(Item):
    pass
class Drink(Item):
    pass
class VendingMachine:
    def __init__(self):
        self.inventory = {
            "A1": Snack("Chips", 1.50, 10),
            "A2": Snack("Candy", 1.00, 15),
            "A3": Drink("Soda", 2.00, 8),
            "A4": Drink("Water", 1.25, 12)
        }
        self.inserted_money = 0.0

    def display_inventory(self):
        print("Available Items:")
        for code, item in self.inventory.items():
            print(f"{code}: {item}")

    def insert_money(self, amount):
        if amount > 0:
            self.inserted_money += amount
            print(f"Inserted ${amount}. Current balance: ${self.inserted_money}")
        else:
            print("Invalid amount.")

    def select_item(self, code):
        item = self.inventory.get(code)
        if item and item.quantity > 0:
            if item.price <= self.inserted_money:
                self.inserted_money -= item.price
                item.quantity -= 1
                print(f"Dispensing {item.name}. Remaining balance: ${self.inserted_money}")
            else:
                print("Insufficient funds.")
        else:
            print("Item not available or invalid code.")

    def return_change(self):
        change = self.inserted_money
        self.inserted_money = 0.0
        print(f"Returning ${change} in change.")
def main():
    vending_machine = VendingMachine()

    while True:
        print("\nVending Machine Menu:")
        print("1. Display Inventory")
        print("2. Insert Money")
        print("3. Select Item")
        print("4. Return Change")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            vending_machine.display_inventory()
        elif choice == 2:
            amount = float(input("Enter the amount to insert: "))
            vending_machine.insert_money(amount)
        elif choice == 3:
            code = input("Enter the item code: ")
            vending_machine.select_item(code)
        elif choice == 4:
            vending_machine.return_change()
        elif choice == 5:
            print("Thank you for using the vending machine!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
print ("1. Display Inventory")
