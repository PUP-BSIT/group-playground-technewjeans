# Genandoy Module
# Exercise 15 Technewjeans

import os
import time
from colorama import init, Fore

init(autoreset=True)

class OrderSystem:
    def __init__(self):
        self.items = [] 
        self.total = 0
        self.customer = ""

    # Properties
    @property
    def item_count(self):
        return len(self.items)

    @property
    def total_value(self):
        return self.total

    # Methods
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_item(self):
        self.clear_screen()
        print(Fore.GREEN + "Add Item")
        name = input("Item name: ")
        price = float(input(f"Price for {name}: "))
        qty = int(input(f"Quantity for {name}: "))
        
        for item in self.items:
            if item['name'] == name:
                item['qty'] += qty
                self.total += price * qty
                print(Fore.YELLOW + 
                      f"Updated {name} with {qty} more units.")
                return

        self.items.append({'name': name, 'price': price, 'qty': qty})
        self.total += price * qty
        print(Fore.YELLOW + f"{name} added with {qty} units!")

    def remove_item(self):
        self.clear_screen()
        print(Fore.RED + "Remove Item")
        print(Fore.CYAN + "Items in order:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['name']} - {item['qty']} units - "
                  f"{Fore.YELLOW}₱{item['price'] * item['qty']:.2f}")
        
        try:
            num = int(input("Number of item to remove: "))
            if 1 <= num <= len(self.items):
                removed = self.items.pop(num - 1)
                self.total -= removed['price'] * removed['qty']
                print(Fore.YELLOW + f"{removed['name']} removed!")
            else:
                print(Fore.RED + "Invalid selection.")
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid selection.")

    def view_order(self):
        self.clear_screen()
        print(Fore.BLUE + "=" * 50)
        print(Fore.CYAN + f"       {self.customer}'s Order       ")
        print(Fore.BLUE + "=" * 50)
        
        if not self.items:
            print(Fore.RED + "Your order is empty!")
        else:
            print(Fore.YELLOW + f"{'Item':<20} {'Qty':<10} "
                  f"{'Price':<10} {'Total':<10}")
            print(Fore.BLUE + "-" * 50)

            for item in self.items:
                total_price = item['price'] * item['qty']
                print(f"{item['name']:<20} {item['qty']:<10} "
                      f"{Fore.YELLOW}₱{item['price']:<9.2f} "
                      f"{Fore.YELLOW}₱{total_price:<9.2f}")
            
            print(Fore.BLUE + "-" * 50)
            print(Fore.GREEN + f"{'Total:':<40} "
                  f"{Fore.YELLOW}₱{self.total:.2f}")
        print(Fore.BLUE + "=" * 50)

    def update_order(self):
        self.clear_screen()
        print(Fore.MAGENTA + "Update Item")
        print(Fore.CYAN + "Items in order:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['name']} - {item['qty']} units - "
                  f"{Fore.YELLOW}₱{item['price'] * item['qty']:.2f}")
        
        try:
            num = int(input("Number of item to update: "))
            if 1 <= num <= len(self.items):
                item = self.items[num - 1]
                new_qty = int(input(f"New quantity for {item['name']}: "))
                self.total -= item['price'] * item['qty']
                item['qty'] = new_qty
                self.total += item['price'] * new_qty
                print(f"{item['name']} updated to {new_qty} units.")
            else:
                print(Fore.RED + "Invalid selection.")
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid selection.")

    def clear_order(self):
        self.clear_screen()
        print(Fore.RED + "Clear All Items")
        self.items.clear()
        self.total = 0 
        print(Fore.YELLOW + "Your order has been cleared!")

    def menu(self):
        while True:
            self .clear_screen()
            print(Fore.GREEN + "=" * 50)
            print(Fore.CYAN + "      Welcome to the Order System      ")
            print(Fore.GREEN + "=" * 50)
            print(Fore.YELLOW + f"Customer: {self.customer if self.customer 
                                         else 'Guest'}")
            print(Fore.BLUE + "-" * 50)
            print(Fore.CYAN + "Choose an option:")

            options = [
                ("1", "Add Item"),
                ("2", "Remove Item"),
                ("3", "View Order"),
                ("4", "Update Order"),
                ("5", "Clear Order"),
                ("6", "Exit")
            ]
            for option in options:
                print(f"{Fore.MAGENTA}{option[0]}. {Fore.WHITE}{option[1]}")

            print(Fore.BLUE + "-" * 50)
            choice = input(Fore.YELLOW + "Enter choice: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.view_order()
            elif choice == "4":
                self.update_order()
            elif choice == "5":
                self.clear_order()
            elif choice == "6":
                print(Fore.RED + "Thank you for using this system!")
                time.sleep(2)
                break
            else:
                print(Fore.RED + "Invalid input. Enter 1-6 only.")
            input(Fore.CYAN + "Press Enter to continue.")

if __name__ == "__main__":
    os.system("cls")
    order_system = OrderSystem()
    order_system.customer = input(Fore.GREEN + "Customer name: ")
    order_system.menu()