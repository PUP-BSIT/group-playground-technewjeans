import os
from showinfm import show_in_file_manager

def main():
    user_input = input("Enter the file or folder path you want to open: ").strip()

    if os.path.exists(user_input):
        show_in_file_manager(user_input)
        print(f"Opened '{user_input}' in your default file manager.")
    else:
        print(f"Error: The path '{user_input}' does not exist. Please check and try again.")

if __name__ == "__main__":
    main()