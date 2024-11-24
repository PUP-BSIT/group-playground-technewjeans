from showinfm import show_in_file_manager

def main():
    # Get user input for the file or folder path
    user_input = input("Enter the file or folder path you want to open: ").strip()

    try:
        # Open the specified file or folder in the file manager
        show_in_file_manager(user_input)
        print(f"Opened '{user_input}' in your default file manager.")
    except Exception as e:
        # Handle errors if the path is invalid or inaccessible
        print(f"Error: {e}")

if __name__ == "__main__":
    main()