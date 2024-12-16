import os
from technewjeans_package.uy import Game
from technewjeans_package.mejares import GBank

def main():
    bank = GBank(profile={}, balance=0.0)#need gumawa ng instance

    while True:
        os.system('cls')
        print("Main Menu:")
        print("1. Krislyn Francisco")
        print("2. Hannah Lorraine Genandoy")
        print("3. James Michael Mejares")
        print("4. Angelica Joy Uy")
        print("5. Clarence Villas")
        print("6. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                os.system('cls')
                pass
            case "2":
                os.system('cls')
                pass
            case "3":
                os.system('cls')
                bank.menu()
            case "4":
                os.system('cls')
                Game.uy_menu()
            case "5":
                os.system('cls')
                pass
            case "6":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()