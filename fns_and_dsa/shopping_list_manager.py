# shopping_list_manager.py
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
            print(f"Added '{new_item}' to the shopping list.")
        elif choice == '2':
            removed_item = input("Enter the item to remove: ")
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"Removed '{removed_item}' from the shopping list.")
            else:
                print(f"Item '{removed_item}' not found in the shopping list.")
        elif choice == '3':
            print(f"Current Shopping List: {shopping_list}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
