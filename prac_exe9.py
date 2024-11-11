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
    director = input("Enter film director: ")
    release_date = input("Enter film release date: ") 
    genre = input("Enter film genre: ")
    language = input("Enter film language: ")

    movies["Title"].append(title)
    movies["Director"].append(director)
    movies["Release date"].append(release_date)
    movies["Genre"].append(genre)
    movies["Language"].append(language)
    print("Film added successfully!\n")
    
def update_movie():
    update_info = input("Enter the list (Title, Director, Release date, Genre, Language) you want to update: ")
    if update_info in movies:
        key_info = int(input("Enter the key index you want to update: "))
        update_value = input (f"Enter the new value for {update_info}: ")
        movies[update_info][key_info] = update_value
    else:
        print("No data record in dictionary")
    
    return " "
    
def delete_movie():
    title_to_delete = input("Enter the title of the movie to delete: ")
    if title_to_delete in movies ["Title"]:
        index = movies["Title"].index(title_to_delete)

        for key in movies:
            movies[key].pop(index)
        print(f"'{title_to_delete}' has been deleted.")

    else:
        print(f"No movie found with the title '{title_to_delete}'.")
    
def search_movie():
    search_term = input("Enter the movie title to search: ")
    if search_term in movies["Title"]:
        index = movies["Title"].index(search_term)
        print("\nSearch Results:")
        print(f"Title: {movies['Title'][index]}")
        print(f"Director: {movies['Director'][index]}")
        print(f"Release Date: {movies['Release date'][index]}")
        print(f"Genre: {movies['Genre'][index]}")
        print(f"Language: {movies['Language'][index]}")
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

if __name__ == "__main__":
    main()