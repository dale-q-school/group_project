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

    # Exit
    if choice == '0':
        print("Thank you for playing! Goodbye!")

    # Tic Tac Toe
    elif choice == '1':
        print("Great Choice! Have Fun!")
        print()

        # Tic Tac Toe code goes here

    # Rock, Paper, Scissors
    elif choice == '2':
        print("Great Choice! Have Fun!")
        print()

        # Rock, Paper, Scissors code goes here

    # Text Adventure
    elif choice == '3':
        print("Great Choice! Have Fun!")
        print()

        # Text Adventure code goes here

    else:
        print("Invalid choice. Please select again.")
