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
    if not movies:
        print("No movies available.")
    else:
        for key in movies:
            print(f"{key}: {movies[key]}")
        
        return " "

   
def add_movie():
    title = input("Enter film title: ")
    author = input("Enter film director: ")
    year = input("Enter film release date: ") 
    genre = input("Enter film genre: ")
    language = input("Enter film language: ")

    add_movie = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "language": language,
    }

    movies.append(movies)
    print("Film added succesfully!/n")

    add_movie()
    print(movies)
    
def update_movie():
    title = input("Enter the title of the movie to update: ")
    for movie in movies:
        if movie["title"] == title:
            # Prompt to update each attribute
            new_title = input("Enter new title (leave blank to keep current): ")
            if new_title:
                movie["title"] = new_title

            new_author = input("Enter new author/director (leave blank to keep current): ")
            if new_author:
                movie["author"] = new_author

            new_year = input("Enter new year of release (leave blank to keep current): ")
            if new_year:
                movie["year"] = int(new_year)

            new_genre = input("Enter new genre (leave blank to keep current): ")
            if new_genre:
                movie["genre"] = new_genre

            new_language = input("Enter new language (leave blank to keep current): ")
            if new_language:
                movie["language"] = new_language

            print("Movie updated successfully.")
            return
    print("Movie not found.")
    
def delete_movie():
    title_to_delete = input("Enter the title of the movie to delete: ")
    found = False

    for movie in movies:
        if movie["Title"] == title_to_delete:
            movies.remove(movie)
            found = True
            print(f"'{title_to_delete}' has been deleted.")
            break

    if not found:
        print(f"No movie found with the title '{title_to_delete}'.")
    
def search_movie():
    search_term = input("Enter the Movie title to search: ")
    found_movies = [movie for movie in movies if search_term in movie['title']]
    if found_movies:
        print("\nSearch Results:")
        for movie in found_movies:
            print(f"Title: {movie['title']},
                    Director: {movie['director']},
                    Release Date: {movie['Release Date']},
                    Genre: {movie['Genre']},
                    Language: {movie['Language']}")
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