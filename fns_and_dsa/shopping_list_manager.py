shopping_list = []

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
            addition = input('What do you want to add to your shopping list ?? \n')
            shopping_list.append(addition)
            pass
        elif choice == '2':
            removed = input("What do you want to remove from your shopping list?? \n")
            shopping_list.remove(str(removed))
            pass
        elif choice == '3':
            for i in range(len(shopping_list)):
                print(f'- {shopping_list[i]}')
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()