from group_package import uy_module, villas_module, genandoy_module, francisco_module, mejares_module

def show_menu():
    print ("--Modules--")
    print ("1. Python Arithmetic Operations")
    print ("2. Display an emoji")
    print ("3. Generate Binary Heatmap")
    print ("4. Calculate the area of a rectangle")
    print ("5. FocusTUI: Your Deep Focus Session Buddy.")
    print ("6. Exit")
    
def menu():
    while True:
        show_menu()
        choice = input ("Enter your choice: ")
        if choice == "1":
            uy_module.main()
        elif choice =="2":
            villas_module.greet_with_emoji()
        elif choice =="3":
            genandoy_module.main() 
        elif choice =="4":
            francisco_module.calculate_area_and_input()
        elif choice =="5":
            mejares_module.focus()
        elif choice =="6":
            print ("Exiting program.")
            break
        else:
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()