#Uy Module
import os

class Films:
    def __init__(self):
        self.owner = "Smith" 
        self.genre_focus = "General"
        self.total_movies = 0 

        self.movies = [] 

    def add_movie(self):
        movie = input("Enter the name of the movie to add: ")
        self.movies.append(movie)
        self.total_movies += 1  # Update total movies
        print(f"Movie '{movie}' added successfully! Total movies: {self.total_movies}")

    def search_movie(self):
        query = input("Enter the name of the movie to search for: ")
        if query in self.movies:
            print(f"Movie '{query}' is in {self.owner}'s collection.")
        else:
            print(f"Movie '{query}' is not in {self.owner}'s collection.")

    def rate_movie(self):
        movie = input("Enter the name of the movie to rate: ")
        if movie in self.movies:
            rating = input(f"Enter a rating for '{movie}' (1-5): ")
            print(f"Rated '{movie}' with {rating} stars.")
        else:
            print(f"Movie '{movie}' not found in {self.owner}'s collection.")

    def remove_movie(self):
        movie = input("Enter the name of the movie to remove: ")
        if movie in self.movies:
            self.movies.remove(movie)
            self.total_movies -= 1  # Update total movies
            print(f"Movie '{movie}' removed successfully! Total movies: {self.total_movies}")
        else:
            print(f"Movie '{movie}' not found in {self.owner}'s collection.")
    
    def list_movies(self):
        print(f"\n{self.owner}'s Movie Collection (Genre: {self.genre_focus}):")
        if self.movies:
            for i, movie in enumerate(self.movies, start=1):
                print(f"{i}. {movie}")
        else:
            print("No movies in the collection.")

    def menu(self):
        while True:
            print(f"\n{self.owner}'s Movie Menu:")
            print("1. Add a Movie")
            print("2. Search for a Movie")
            print("3. Rate a Movie")
            print("4. Remove a Movie")
            print("5. List Movies")
            print("6. Back to Main Menu")
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    self.add_movie()
                case "2":
                    self.search_movie()
                case "3":
                    self.rate_movie()
                case "4":
                    self.remove_movie()
                case "5":
                    self.list_movies()
                case "6":
                    print("Returning to the main menu...")
                    break
                case _:
                    print("Invalid choice. Please try again.")

