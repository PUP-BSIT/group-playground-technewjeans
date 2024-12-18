#mejares module with class
import os
import random

class GamblingAddiction:
    def __init__(self, profile, balance,luck):
        self.profile = profile
        self.balance = balance
        self.transactions = []
        self.luck = luck

    def get_profile(self): #1
        print('--Create my Profile Section--')
        self.profile['name'] = input('Enter your name: ')
        self.profile['phone number'] = input('Enter your phone number: ')
        self.profile['password'] = input('Enter your password: ')
        print('--Account saved successfully--')

    def display_profile(self): #2
        if self.profile:

            print('--My Profile--')
            print(f'Name: {self.profile['name']}')
            print(f'Phone Number: {self.profile['phone number']}')
            print(f'Password: {self.profile['password']}')
            print(f'Balance: {self.balance:.2f}')
            print(f'Your current luck: {self.luck:.2f}')
        else:
            print('--No account found. Please create one.--')
    
    def deposit(self):  #3
        if self.profile:
            amount = float(input('Enter the amount to deposit: ₱'))
            self.balance += amount
            self.luck += amount * 0.1
            self.transactions.append(f'Deposited ₱{amount}')

            print(f'\nYou have deposited ₱{amount} successfully')
            print(f'Your new balance is ₱{self.balance:.2f}')
            print(f'You gained {self.luck:.2f}% luck')
            print('--Transaction recorded successfully--')
        else:
            print('--No account found. Please create one.--')
        
    def waste_money_game(self): #4
        color = input('Enter color (red, blue, white, green, yellow): ')
        bet_amount = float(input('Enter the amount you want to bet: ₱'))
        
        valid_colors = ['red', 'blue', 'white', 'green', 'yellow']
        winning_color = random.choice(valid_colors)
        print(f'The winning color is: {winning_color}')
            
        if color == winning_color:
            prize = bet_amount * 2
            self.balance += prize
            print(f'WIN: ₱{prize:.2f} | Balance: ₱{self.balance:.2f}')
        else:
            self.balance -= bet_amount
            print(f'LOSE: ₱{bet_amount:.2f} | Balance: ₱{self.balance:.2f}')
        
    def display_transactions(self):#5
        if self.transactions:
            print('--My Transactions--')
            for transaction in self.transactions:
                print(transaction)
        else:
            print('--There are no transactions has been made.--')

    def mejares_menu(self):
        while True:
            os.system('cls')
            print('--C0L0R GAME MENU--')
            print("1. Create Profile")
            print("2. Display Profile")
            print("3. Cash-In M0ney")
            print("4. Play C0L0R GAME")
            print("5. Display transactions")
            print("6. Go back to main >>")
            user_choice = input('Enter choice: ')

            match user_choice:
                case "1":
                    os.system('cls')
                    self.get_profile()
                    input("\nPress enter to continue.")
                case "2":
                    os.system('cls')
                    self.display_profile()
                    input("\nPress enter to continue.")
                case "3":
                    os.system('cls')
                    self.deposit()
                    input("\nPress enter to continue.")
                case "4":
                    os.system('cls')
                    if self.profile and self.balance > 0:
                        print('---Welcome to C0L0R GAME---')
                        print(f'Balance: ₱{self.balance:.2f}')
                        print(f'Chances of winning: {self.luck:.2f}%')
                        print('--Choose color you want to bet your money on--')
                        self.waste_money_game()
                    else:
                        print('--No account found or insufficient balance.--')

                    input("\nPress enter to continue.")
                case "5":
                    os.system('cls')
                    self.display_transactions()
                    input("\nPress enter to continue.")
                case "6":
                    print("Commence return to main...")
                    break
                case _:
                    print("Invalid choice, please select a valid option.")