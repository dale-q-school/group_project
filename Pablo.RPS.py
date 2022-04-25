import random

print('Welcome to Rock Paper Scissors!\n')
#This will be the constant
losses = 0 
wins = 0
ties = 0
current_rounds = 0
rpslist = ['rock','paper','scissors']

#Start of the loop and trying to make a wrong option answer
while True:
    mach = random.choice(rpslist)
    user_input = input('\nChoose (rock, paper, scissors):')
    if user_input.lower() == 'rock':
        True
    elif user_input.lower() == 'paper':
       True
    elif user_input.lower() == 'scissors':
        True
    else:
        print('\nWow that must have being a mistake')
        test1 = input('\nwould you like to try again (y/n) ')
        if test1.lower() != 'y':
            break
              #Here is where the main code starts defining when is a tie a win or a lost
    if user_input.lower() == mach:
        current_rounds = current_rounds + 1
        ties = ties + 1
        print('What are the odds')
        print('\nBoth of you choose' , user_input , 'It\'s a tie!')
        
    elif user_input.lower() == 'rock':
        if mach == 'scissors':
            current_rounds = current_rounds + 1
            wins = wins + 1
            print('\nRock wins against Scissors! You Win!')
        else:
            current_rounds = current_rounds + 1
            losses = losses + 1
            print('\nPaper wins against Rock, You lose')
        
    elif user_input.lower() == 'paper':
        if mach == 'rock':
            current_rounds = current_rounds + 1
            wins = wins + 1
            print('\nPaper wins against Rock! You Win!')
        else:
            current_rounds = current_rounds + 1
            losses = losses + 1
            print('\nScissors wins against Paper, You lose')
            
    elif user_input.lower() == 'scissors':
        if mach == 'paper':
            current_rounds = current_rounds + 1
            wins = wins + 1
            print('\nScissors wins against Paper! You Win!')
        else:
            current_rounds = current_rounds + 1
            losses = losses + 1
            print('\nRock wins against Scissors, You lose')
            #I'm still not sure about this part but I wanna see if I can change it
    print('Rounds:', current_rounds, 'Wins:', wins, 'Loss:', losses, 'ties:', ties)
    run_back = input('\nWant to run it back?' '(y/n)')
    if run_back.lower() != 'y':
        break
    