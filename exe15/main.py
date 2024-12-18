import os
from technewjeans_package.uy import Game
from technewjeans_package.mejares import Gamble
from technewjeans_package.genandoy import OrderSystem
from technewjeans_package.villas import Music
from technewjeans_package.francisco import Information

def main():
    order_system = OrderSystem() 

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
                information = Information(age=19, city="Taguig City", school="PUP-Taguig")
                information.menu()
            case "2":
                os.system('cls')
                order_system.customer = input("Enter customer name: ")
                order_system.menu()
            case "3":
                os.system('cls')
                gamble = Gamble(profile={}, balance=0.0, luck=0.0)
                gamble.display_user_choices()
            case "4":
                os.system('cls')
                Game.uy_menu()
            case "5":
                os.system('cls')
                song_title = input("Enter the Song Title: ")
                song_writer = input("Enter the Song Writer: ")
                genre = input("Enter the Genre: ")
                year_release = input("Enter the Year of Release: ")
                music1 = Music(song_title, song_writer, genre, year_release)
    
                music1.menu()
            case "6":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()