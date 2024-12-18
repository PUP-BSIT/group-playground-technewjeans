#mejares module with class
import os
import random

EXIT_OPTION = 6
UNSET_OPTION = -1

class Gamble:
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
    
    def get_deposit(self):  #3
        if self.profile:
            amount = float(input('Enter amount to deposit: ₱'))
            self.balance += amount
            self.luck += amount * 0.1
            self.transactions.append(f'Deposited ₱{amount}')

            print(f'\nYou have deposited ₱{amount} successfully')
            print(f'Your new balance is ₱{self.balance:.2f}')
            print(f'You gained {self.luck:.2f}% luck')
            print('--Transaction recorded successfully--')
        else:
            print('--No account found. Please create one.--')
        
    def display_game(self): #4
        color = input('Enter color (red, blue, white, green, yellow): ')
        bet_amount = float(input('Enter the amount you want to bet: ₱'))
        
        valid_colors = ['red', 'blue', 'white', 'green', 'yellow']
        winning_color = random.choice(valid_colors)
        print(f'\nThe winning color is: {winning_color}')
            
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

    def display_user_choices(self):
        os.system('cls')
        user_choice = UNSET_OPTION
        while user_choice != EXIT_OPTION:
            user_choice = self.get_user_choice()
            self.operate_choice(user_choice)
            os.system('cls')

    def get_user_choice(self):
            os.system('cls')
            print('--C0L0R GAME MENU--')
            print("1. Create Profile")
            print("2. Display Profile")
            print("3. Cash-In M0ney")
            print("4. Play C0L0R GAME")
            print("5. Display transactions")
            print("6. Go back to main >>")

            return int(input('Enter choice: '))
                
    def operate_choice(self,user_choice):
            match user_choice:
                case 1:
                    os.system('cls')
                    self.get_profile()
                    input("\nPress enter to continue.")
                case 2:
                    os.system('cls')
                    self.display_profile()
                    input("\nPress enter to continue.")
                case 3:
                    os.system('cls')
                    self.get_deposit()
                    input("\nPress enter to continue.")
                case 4:
                    os.system('cls')
                    if self.profile and self.balance > 0:
                        print('---Welcome to C0L0R GAME---')
                        print(f'Balance: ₱{self.balance:.2f}')
                        print(f'Chances of winning: {self.luck:.2f}%')
                        print('--Choose color you want to bet your money on--')
                        self.display_game()
                    else:
                        print('--No account found or insufficient balance.--')

                    input("\nPress enter to continue.")
                case 5:
                    os.system('cls')
                    self.display_transactions()
                    input("\nPress enter to continue.")
                case 6:
                    print("Commence return to main...")
                    pass
                case _:
                    print("Invalid choice, please select a valid option.")