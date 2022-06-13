import random

possibleOptions = ['R', 'P', 'S'] 
print("Welcome to Rock-Paper-Scissors")


#game is initialised. Player makes their move
def init():  
    global playerChoice  #make playerChoice a global variable ie scope is not local to only this function.
    playerChoice = input("Please make your move: \n 'R' for Rock\n 'P' for Paper\n 'S' for Scissors\n").upper()
    if playerChoice in possibleOptions:
        play_game()
    else:
        invalid_option()
        

#if player's input is invalid, function activates
def invalid_option():
    
    print("Invalid Input. Try Again!")
    init()


#CPU counters player's moves. There's a better way to represent these lines using functions. I prefer this method.
def play_game():    
    computerChoice = random.choice(possibleOptions)    
    if playerChoice == 'R' and computerChoice == 'R':
        print("Player (Rock): CPU (Rock)")
    elif playerChoice == 'R' and computerChoice == 'P':
        print("Player (Rock): CPU (Paper)")
    elif playerChoice == 'R' and computerChoice == 'S':
        print("Player (Rock): CPU (Scissors)")
    elif playerChoice == 'P' and computerChoice == 'R':
        print("Player (Paper): CPU (Rock)")
    elif playerChoice == 'P' and computerChoice == 'P':
        print("Player (Paper): CPU (Paper)")
    elif playerChoice == 'P' and computerChoice == 'S':
        print("Player (Paper): CPU (Scissors)")
    elif playerChoice == 'S' and computerChoice == 'R': 
        print("Player (Scissors): CPU (Rock)")
    elif playerChoice == 'S' and computerChoice == 'P':
        print("Player (Scissors): CPU (Paper)")
    elif playerChoice == 'S' and computerChoice == 'S':
        print("Player (Scissors): CPU (Scissors)")
    else: 
        print("Invalid Selection. Try Again!")

#rules of the game
    if playerChoice == computerChoice:
        print("It's a tie. Try Again")
        init()
    elif playerChoice == "R":
        if computerChoice == "S":
            print("Rock Crushes Scissors! Player Wins!")
        else:
            print("Paper covers Rock! CPU Wins!")
    elif playerChoice == "P":
        if computerChoice == "R":
            print("Paper Covers Rock! Player Wins!")
        else:
            print("Scissors cuts Paper! CPU Wins!")
    elif playerChoice == "S":
        if computerChoice == "P":
            print("Scissors Cuts Paper! Player Wins!")
        else:
            print("Rock Crushes Scissors! CPU Wins!")

init()

