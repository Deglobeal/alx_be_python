def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list

    while True:
        display_menu()  # Show the menu
        
        # Ensure valid numeric input for menu choice
        choice = input("Enter your choice: ")
        
        # Check if the input is a valid number (1 to 4)
        if choice.isdigit():
            choice = int(choice)  # Convert input to an integer
            
            if choice == 1:
                # Prompt for and add an item
                item = input("Enter the item you want to add: ").strip()
                shopping_list.append(item)  # Add the item to the list
                print(f"'{item}' has been added to your shopping list.")
            
            elif choice == 2:
                # Prompt for and remove an item
                item = input("Enter the item you want to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)  # Remove the item from the list
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")
            
            elif choice == 3:
                # Display the shopping list
                if shopping_list:
                    print("Current Shopping List:")
                    for idx, item in enumerate(shopping_list, start=1):
                        print(f"{idx}. {item}")
                else:
                    print("Your shopping list is empty.")
            
            elif choice == 4:
                print("Goodbye!")  # Exit message
                break  # Exit the loop
            
            else:
                print("Invalid choice. Please try again.")  # Handle invalid choices
        else:
            print("Invalid input. Please enter a number between 1 and 4.")  # Handle non-numeric input

if __name__ == "__main__":
    main()  # Start the program
