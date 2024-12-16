# villas.py
import os

class Music:
    def __init__(self, song_title, song_writer, genre, year_release):
        self.song_title = song_title
        self.song_writer = song_writer
        self.genre = genre
        self.year_release = year_release
    
    def display_song_title(self):
        print(f"Song Title: {self.song_title}")
        
    def display_song_writer(self):
        print(f"Song Writer: {self.song_writer}")
    
    def display_genre(self):
        print(f"Genre: {self.genre}")
    
    def display_year_release(self):
        print(f"Year Release: {self.year_release}")

    def add_song(self):
        print("\nAdd a New Song")
        self.song_title = input("Enter the new Song Title: ")
        self.song_writer = input("Enter the new Song Writer: ")
        self.genre = input("Enter the new Genre: ")
        self.year_release = input("Enter the new Year of Release: ")
        print("\nNew song added successfully!")

    def menu(self):
        while True:
            print("\n---- Clarence Villas Main Menu ----")
            print("1. Display Song Title")
            print("2. Display Song Writer")
            print("3. Display Genre")
            print("4. Display Year Release")
            print("5. Add New Song")
            print("6. Exit")

            choice = input("Please enter a number: ")

            match choice:
                case '1':
                    self.display_song_title()
                case '2':
                    self.display_song_writer()
                case '3':
                    self.display_genre()
                case '4':
                    self.display_year_release()
                case '5':
                    self.add_song()
                case '6':
                    print("Exiting the menu. Bye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")

song_title = input("Enter the Song Title: ")
song_writer = input("Enter the Song Writer: ")
genre = input("Enter the Genre: ")
year_release = input("Enter the Year of Release: ")

music1 = Music(song_title, song_writer, genre, year_release)

music1.menu()