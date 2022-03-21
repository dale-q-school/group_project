# Main Menu
choice = None
while choice != '0':
    print(
        """
        Choose a game to play!
        
        0 - Quit
        1 - Tic Tac Toe
        2 - Rock, Paper, Scissors
        3 - Text Adventure
        """
    )

    choice = input("Choice: ")
    print()

    if choice == '0':
        print("Thank you for playing! Goodbye!")

    elif choice == '1':
        print("Great Choice! Have Fun!")

    elif choice == '2':
        print("Great Choice! Have Fun!")

    elif choice == '3':
        print("Great Choice! Have Fun!")

    else:
        print("Invalid choice. Please select again.")
