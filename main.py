from PabloRPS import *
from TriviaQuiz import *
from textadventure import *
from clearscreen import *

# Main Menu
clear()
choice = None
while choice != '0':
    print(
        """
        Choose a game to play!
        
        0 - Quit
        1 - Pablo's Rock, Paper, Scissors
        2 - Kaneko's Word Trivia
        3 - Dale's Text Adventure
        """
    )

    choice = input("Choice: ")
    print()

    # Exit
    if choice == '0':
        print("Thank you for playing! Goodbye!")

    # Pablo's Rock, Paper, Scissors
    elif choice == '1':
        clear()
        rockPaperScissors()

    # Kaneko's Word Trivia
    elif choice == '2':
        clear()
        triviaGame()

    # Dale's Text Adventure
    elif choice == '3':
        clear()
        textadventure()

    else:
        print("Invalid choice. Please select again.")
