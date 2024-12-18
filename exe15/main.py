import os
from technewjeans_package.francisco import Information
from technewjeans_package.genandoy import OrderSystem
from technewjeans_package.mejares import GamblingAddiction
from technewjeans_package.uy import Game
from technewjeans_package.villas import Music

EXIT_OPTION = " "
UNSET_OPTION = "6"

def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_choice()
        process_choice(choice)

def display_choice():
    os.system('cls')
    print("Main Menu:")
    print("1. Krislyn Francisco")
    print("2. Hannah Lorraine Genandoy")
    print("3. James Michael Mejares")
    print("4. Angelica Joy Uy")
    print("5. Clarence Villas")
    print("6. Exit")

    return input("Enter your choice: ")

def process_choice(choice):
    order_system = OrderSystem()
    
    match choice:
        case "1":
            os.system('cls')
            information = Information(age=19, city="Taguig City", school="PUP-Taguig")
            information.menu()
        case "2":
            os.system('cls')
            order_system.customer = input("Enter customer name: ")
            order_system.menu()
        case "3":
            os.system('cls')
            gamble = GamblingAddiction(profile={}, balance=0.0, luck=0.0)
            gamble.mejares_menu()
        case "4":
            os.system('cls')
            Game.game_menu()
        case "5":
            os.system('cls')
            song_title = input("Enter the Song Title: ")
            song_writer = input("Enter the Song Writer: ")
            genre = input("Enter the Genre: ")
            year_release = input("Enter the Year of Release: ")
            music1 = Music(song_title, song_writer, genre, year_release)
            music1.menu()
        case "6":
            pass
        case _:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()