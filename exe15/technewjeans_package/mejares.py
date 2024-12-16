import os
import time

class GBank:#my class
    def __init__(self, profile, balance):#my constructor
        self.profile = profile#my three property(ies)
        self.balance = balance
        self.transactions = []

    def get_profile(self): #method1 
        print('--Create my Profile Section--')
        self.profile['name'] = input('Enter your name: ')
        self.profile['id'] = input('Enter your id: ')
        self.profile['phone number'] = input('Enter your phone number: ')
        time.sleep(2)
        print('--Account saved successfully--')

    def display_profile(self): #metjod2
        if self.profile:
            time.sleep(2)
            print('--My Profile--')
            print(f'Name: {self.profile["name"]}')
            print(f'ID: {self.profile["id"]}')
            print(f'Phone Number: {self.profile["phone number"]}')
            print(f'Balance: {self.balance:.2f}')
        else:
            print('--No account found. Please create one.--')

    def deposit(self): #method3
        amount = float(input('Enter the amount to deposit: ₱'))
        self.balance += amount
        self.transactions.append(f'Deposited ₱{amount}')
        time.sleep(2)
        print(f'\nYou have deposited ₱{amount} successfully')
        print(f'Your new balance is ₱{self.balance:.2f}')
        print('--Transaction recorded successfully--')

    def send_money(self): #method4
        amount = float(input('Enter the amount to send: ₱'))
        recipient = input('Enter the recipient\'s name: ')
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Sent ₱{amount} to {recipient}')
            time.sleep(2)
            print(f'\nYou have sent ₱{amount} to {recipient} successfully')
            print(f'Your new balance is ₱{self.balance:.2f}')
            print('--Transaction recorded successfully--')
        else:
            print('You have insufficient balance')

    def display_transactions(self):#method 5
        if self.transactions:
            time.sleep(2)
            print('--My Transactions--')
            for transaction in self.transactions:
                print(transaction)
        else:
            print('--There are no transactions has been made.--')

    def menu(self):
        while True:
            os.system('cls')
            print('--Bank Menu--')
            print('1. Create a Profile')
            print('2. Display Profile')
            print('3. Deposit money')
            print ('4. Send express money')
            print('5. Display all transactions')
            print('6. Go to main menu')

            try:
                user_choice = int(input("\nEnter the number of your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number again.")
                input("\nPress enter to continue.")
                continue
            
            if user_choice == 0:
                break

            match user_choice:
                case 1:
                    os.system('cls')
                    self.get_profile()

                case 2:
                    os.system('cls')
                    self.display_profile()

                case 3:
                    os.system('cls')
                    self.deposit()

                case 4:
                    os.system('cls')
                    self.send_money()

                case 5:
                    os.system('cls')
                    self.display_transactions()
                
                case 6:
                    print("Returning to the main menu...")
                    time.sleep(2)
                    break

                case _:
                    print("Invalid choice. Please select a valid option.")

            input("\nPress enter to continue.")
            

            
        

        

