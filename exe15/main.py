import os
from package.uy import Films

def main():
    films = Films()

    while True:
        os.system('cls')
        print("\nMain Menu:")
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
                films.menu()
            case "2":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()