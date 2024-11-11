#Technewjeans Exercise 9

movies = {
    "Title": ["Portrait of a Lady on Fire"], 
    "Director": ["Céline Sciamma"], 
    "Release date": ["September 18, 2019"], 
    "Genre": ["Historical Drama"], 
    "Language": ["French"]
}

# Main menu function
def show_menu():
    print("\n----- Netflix Movies Recommendations -----")
    print("1. List All Movies")
    print("2. Add a Movie")
    print("3. Update a Movie")
    print("4. Delete a Movie")
    print("5. Search for a Movie")
    print("6. Exit")

# Function to list all movies
def list_all_movies():
    # TODO: Clarence 
    def list_all_movies(movies):
    if not movies:
        print("No movies available.")
    else:
        print("\nMovies:")
    for idx, movie in enumerate(movies, start=1):
            print(f"{idx}. Title: {movie['Title']}, 
        Title: {movie['Director']},
        Director: {movie['Genre']}, 
        Year Released: {movie['Year Released']}, 
        Genre: {movie['Genre']}")
        Language: ()

   
def add_movie():
    # TODO: Member James
    
def update_movie():
    # TODO: Member Joy
   
def delete_movie():
    # TODO: Hannah
    title_to_delete = input("Enter the title of the movie to delete: ")
    found = False

    for movie in movies:
        if movie["Title"].lower() == title_to_delete.lower():
            movies.remove(movie)
            found = True
            print(f"'{title_to_delete}' has been deleted.")
            break

    if not found:
        print(f"No movie found with the title '{title_to_delete}'.")
    
def search_movie():
    # TODO: Krislyn
    search_term = input("Enter the Movie title to search: ")
    found_movies = [movie for movie in movies if search_term in movie['title']]
    if found_movies:
        print("\nSearch Results:")
        for movie in found_movies:
            print(f"Title: {movie['title']} | Director: {movie['director']} | Release Date: {movie['Release Date']} | Genre: {movie['Genre']} | Language: {movie['Language']}")
    else:
        print("No movies found.")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            list_all_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            search_movie()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")