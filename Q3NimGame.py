# Jahkim Brown-Roopnarine
# ICS 3U0 - A
# November 22, 2021
# This program will run the ancient Chinese Game of Nim. The program will choose a number of stones between 15 and 30 as
# two players swap turns taking their choice of 1, 2, or 3 stones from the lot. The player that is forced to take up the
# last stone loses the game. Players can not intentionally choose to take the last stone, if not compulsory. This program
# will allow the option to play multiplayer or single player. The single player mode will also have two levels of
# difficulty that may be played.

import random # imports the random library to be used later throughout the code.

compWins = 0 # iniatilizes value for global variable to be used later in program - will be used to count computer wins throughout games execution.
playerWins = 0 # " " - counts player wins.
player1Wins = 0 # " " - counts player1 wins (used in multiplayer mode).
player2Wins = 0 # " " - counts player2 wins (used in multiplyer mode).

# INPUT based function
def getInput(prompt, helpString): # input based function, used for all methods of in-game online documentation, menu based navigation, and program termination.
    resp = input(prompt) # takes input from the prompt string.
    if resp == "quit": # if input from the function is equal to quit, the program will terminate.
        print("\n" + "Thank you for playing the Game of Nim " + name + "!") # exit message.
        quit(0) # terminates code.
    elif resp == "main menu": # if input from the function is equal to main menu, the program will return to the main menu.
        print("Returning to the main menu...") # message printed, telling user that they are returning to main menu.
        mainMenu() # calls main menu function.
    elif resp == "help": # if input from the function is equal to help, the program will display a given help string, the the function will recur, to return the user to where help was called.
        print(helpString) # prints help string.
        return getInput(prompt, helpString) # function recurs to return user to where help was called.
    else:
        return resp # if no key terms were typed for external action, function will return the input of the function where necessary.

# Introduction based function
def introduction():
    name = input("Hi there, what is your name? ") # asks user for their name, using basic input function, as name could potentially be a key word.
    print("Hello " + name + "!\n" 
          "  _      _____ _     ____  ____  _      _____    _____  ____     _      _  _     _ \n"
          " / \  / |/  __// \   /   _\/  _ \/ \__/|/  __/   /__ __\/  _ \   / \  /|/ \/ \__/ |\n"
          " | |  | ||  \  | |   |  /  | / \|| |\/|||  \       / \  | / \|   | |\ ||| || |\/| |\n"
          " | |/\| ||  /_ | |_/\|  \_ | \_/|| |  |||  /_      | |  | \_/|   | | \||| || |  | |\n"
          " \_/  \ |\____/\____/\____/\____/\_/  \|\____\     \_/  \____/   \_/  \|\_/\_/  \ |\n"
          "If at any point you would like the program to terminate, type 'quit'.\n"
          "If at any point you require help, please type 'help'.\n"
          "If at any point you would like to return to the main menu, please type 'main menu'\n")  # print statement for greeting message, welcomes user, and introduces keywords for navigation and online documentation.
    return name # returns name so that it may be used throughout the program.

# Function for displaying the main menu
def mainMenu():
    print("\n"
          "Welcome to the Main Menu\n"
          "[1] Rulebook\n"
          "[2] Singleplayer\n"
          "[3] Multiplayer\n"
          "[4] Exit") # prints main menu options with correlated numbers.

    stopper = False # stopper value used for while loop that will execute try and except.
    while not stopper: # while stopper is false the following loop will be executed
        try:
            selection = int(getInput("Enter your selection: ", "It seems like you're having some trouble. Please type one of the options to enter a selection.")) # takes integer input for a menu selection, has help documentation if needed
            if selection not in range(1, 5): # if number is not between 1 and 4, a value error will be created to ensure that valid inputs are taken.
                raise ValueError
            break # breaks loop
            stopper = True # stopper is set to true so that the loop will not run for another iteration
        except (ValueError, TypeError): # if a ValueError or TypeError takes place, the following will be displayed. Handles exceptions for potential float or string inputs, and inaccurate number ranges.
            print("Error detected. Please re-input your selection") # print statement telling user of error.
            stopper = False # stopper remains false, so that loop may run for another iteration.

    while selection != 0: # while selection is not zero, the following will occur.
        if selection == 1: # if selection is equal to 1, rulebook will be called.
            rulebook() # rulebook function called.
            break # breaks loop
        elif selection == 2: # " "
            getSingleplayer() # getSingleplayer function called to execute singleplayer mode.
            break # " "
        elif selection == 3: # " "
            getMultiplayer() # function called to execute multiplayer mode.
            break # " "
        elif selection == 4: # " "
            print("Exit has been selected\n" 
                  "Thank you for playing the Game of Nim " + name + "!") # Exit message.
            quit(0) # Terminates code.
        else:
            print("Error detected. Please re-input your selection") # else clause that will not be fulfilled, there for accessory.

# Function for displaying the rules to the user
def rulebook():
    print("\n"
          "Rulebook has been selected.\n"
          "The program will choose a number of stones between 15 and 30 as two players swap turns taking their\n"
          "choice of 1, 2, or 3 stones from the lot. The player that is forced to take up the last stone loses the game.\n"
          "Players can not intentionally choose to take the last stone, if not compulsory. This program will allow the option\n"
          "to play multiplayer or single player. The single player mode will also have two levels of difficulty that may be played.") # tells users the rules to play

    typeAnything = getInput("Hope that helps! Type anything to dismiss this message.", "It seems like you're having some trouble. Type anything to dismiss this message.") # Gives the user a dismiss message line

    while typeAnything == typeAnything: # anything the user does will retun them to the main menu, besides typing a keyword from the getInput function
       mainMenu() # calls main menu function

def getStones(): # function for initializing gameplay with stones
    stones = random.randint(15,30) # picks random number of stones between 15 and 30 to begin a game.
    return stones # function returns stones for later functions.

def getHeadsorTails(): # Heads or tails functions for determining which player goes first in gameplay.
    list = ["Heads", "Tails"] # list of two options
    coinFlip = random.choice(list) # random choice between a list of heads or tails will simulate flipping a coin with 50/50 odds
    return coinFlip # retunrs the flipped coin for later functions

############################################################################################################################################################################
# Function for initializing single player gameplay
def getSingleplayer():
    print("\n"
          "Singleplayer has been selected.\n"
          "Welcome once more to the ancient game of Nim! If you couldn't tell by now, you should be warned that you are\n"
          "going to have quite the struggle beating me!\n") # welcome message for the user

    checkIn = getInput("But before we begin, do you know how to play? (yes/no) ", "It seems like you're having some trouble. Type yes to continue or no to see the rules.") # check in to see if user knows how to play

    if checkIn == "no": # if no is typed, the user will be returned to the rulebook and then to the main menu to reenter their preferred mode of play.
        print("No worries: take a look at the rules and come back after!") # print statement telling the user to check the rules
        rulebook() # calls the rulebook function
    else: # if anything besides no or a keyword from getInput is typed the following will occur.
        stopper = False # stopper set to false for while loop
        while not stopper: # while stopper is false the following loop will occur.
            try: # try and except used to handle exceptions from options provided.
                initDifficulty = int(getInput("Okay great! Now that we got that out of the way. Please select a diffuclty:\n"
                                              "[1] Regular\n"
                                              "[2] Hard\n", "It seems like you're having some trouble. Type '1' to play the regular diffuculty, or '2' to play the hard difficulty.")) # input for integer, helpstring if needed.
                if initDifficulty not in range(1,3): # if initializing for difficulty is not 1 or 2, error raised.
                    raise ValueError
                break # breaks loop if try is fulfilled.
                stopper = True # stopper is set to true, so loop will not run for another iteration.
            except (ValueError, TypeError): # if float, or string is detected, error is raised
                print("Error detected. Please re-input your selection") # error detection message
                stopper = False # stopper is set to true so that loop will run for another iteration.

        if initDifficulty == 1: # if 1 is inputted for difficulty selection then regular difficutly is selected
            getSpReg() # calls regular difficulty function
        elif initDifficulty == 2: # " "
            getSpHard() # cals hard difficulty function
        else:
            print("Error detected. Please re-input your selection") # accessory else clause.

########################################################################################################################################################################
# all below in the next segments are functions used for regular difficulty gameplay.

def cpuReg(stones): # function for computer playing on regular difficulty.
    global playerWins # calls global variables for win tracking.
    global compWins # " "

    if stones > 3: # if stones are greater than 3, the following will happen.
        cpuChoice = random.randint(1, 3) # computer will pick a random number between 1 and 3 to make its choice.
        if cpuChoice > stones: # if the cpu's choice is greater than stones, then it will try again - accesory code.
            cpuReg(stones) # will recall itself, if cpu choice is invalid.
        else: # with the computers final choice the following will happen.
            stones = stones - cpuChoice # new stone value determined by subtracting comp choice from the initial stones value.
            print("I have taken", cpuChoice, "from the pile. There now remains", stones, "left.") # computer print to inform user of their play.
            if stones == 0: # if stones is equal to zero on the computers turn, then the computer loses, and the user wins.
                print("You win!") # tells user they win.
                playerWins += 1 # adds one win to player global variable.

                print("Player wins =", playerWins, "\n"
                      "Computer wins =", compWins) # displays total win counts

                replay = getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ") # asks user if they would like to play again
                if replay == replay: # if user types anything besides a keyword from the getInput function (allowing them to quit, get help, or return to main menu) regular difficulty will run again
                    getSpReg() # calls function iniaitilizes regular singleplayer mode
            else:
                playerGameplay(stones) # if stones is not 0, then will call the playergameplay function, for the user to make their play. The two functions will alternate until stones is equal to 0.

    if stones == 3: # if stones is equal to zero, the following will take place.
        cpuChoice = random.randint(1,2) # chooses random choice between 1 and 2 to ensure that cpu does not purposely lose game.
        stones = stones - cpuChoice # " "
        print("I have taken", cpuChoice, "from the pile. There now remains", stones, "left.") # " "
        if stones == 0: # " "
            print("You win!") # " "
            playerWins += 1 # " "

            print("Player wins =", playerWins, "\n"
                  "Computer wins =", compWins) # " "

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ",
                              "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ") # " "
            if replay == replay: # " "
                getSpReg() # " "
        else:
            playerGameplay(stones) # " "

    if stones <= 2: # if stones are equal to or less than 2, then the following will happen.
        cpuChoice = 1 # cpu choice must be 1 to ensure that the program does not forcefully lose, and may accept defeat when beaten by user.
        stones = stones - cpuChoice # ""
        print("I have taken", cpuChoice, "from the pile. There now remains", stones, "left.") #""
        if stones == 0: # ""
            print("You win!") # ""
            playerWins += 1 # " "

            print("Player wins =", playerWins, "\n"
                  "Computer wins =", compWins) # " "

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ",
                              "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ") # " "
            if replay == replay: # ""
                getSpReg() # ""
        else:
            playerGameplay(stones) # ""

def playerGameplay(stones): # function for human user playing on regular gameplay.
    global compWins # ""
    global playerWins # ""

    if stones > 0: # if stones are greater than 0, then the following may happen.
        stopper = False # sets stopper to false, so that try and except loop may run.
        while not stopper: # while stopper is false, the loop may run.
            try: # try and except used for handling exceptions inputted from user.
                playerChoice = int(getInput("Select how many stones you would like to remove from the pile: ", "It seems you are a bit stuck. Enter a number between 1 and 3 to remove a desired amount of stones from the pile. Remember you can not purposely take the last stone from the pile!")) # gets integer input, with help information
                if playerChoice > stones or playerChoice not in range (1,4): # if number is not in desired range, error is given.
                    raise ValueError
                if stones == 3 and playerChoice == 3: # if player forcefully loses the game, error is given for prevention.
                    raise ValueError
                if stones == 2 and playerChoice == 2: # if player forcefully loses the game, erros is given for prevention.
                    raise ValueError

                stopper = True # stopper is set to True, if try is fulfilled without exceptions.
                break # breaks out of loop
            except (ValueError, TypeError): # if exception is detected where float, string, or forceful loss is given, the error message will display.
                print("Error detected. Please reinput choice.") # error message.
                playerGameplay(stones) # calls for player to reinput their choice.

        stones = stones - playerChoice #"" subtracts human choice
        print("You have taken", playerChoice, "from the pile. There now remains", stones, "left.") # tells user their choice.
        if stones == 0: # if stones equal to zero, on user turn, they lose.
            print("You lose!") # tells user they lose.
            compWins += 1 # adds win to computer tally.

            print("Player wins =", playerWins, "\n" 
                  "Computer wins =", compWins) # tells user scoreboard.

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ") # ""
            if replay == replay: # ""
                getSpReg() # ""
        else:
            cpuReg(stones) # if user does not lose on their turn, will call the computer to complete a turn.

# Function that orchestrates gameplay after called from menu
def getSpReg():
    print("\nSingle player Regular difficulty has been selected.\n"
          "Let's flip a coin to see who goes first. Heads it's you, tails it's me.") # informs user of difficulty selected.

    flipper = getInput("Press Enter to flip a coin ", "It seems you are a bit stuck. Press enter to flip a coin") # input for user to flip a coin

    if flipper == flipper: # if user does anything that is not a keyword from getInput, the following will occur
        coinFlip = getHeadsorTails() # will flip a coin, using the coin flipping function.
        stones = getStones() # will get stones from appropriate function.

    if coinFlip == "Heads": # if heads is flipped, user will go first
        print("\nHeads! Okay, so you go first!") # tells user they go first
        print("This game will be played with", stones,"stones") # tells user how many stones are being played with
        playerGameplay(stones) # calls playerGameplay function with stones passed into it for computation

    elif coinFlip == "Tails": # " " computer goes first
        print("\nTails! Okay, so I go first!") # " " cpu 1st
        print("This game will be played with", stones,"stones") #" "
        cpuReg(stones) # calls cpu regular difficulty function with stones passed into it for computation

###########################################################################################################################################################################################
# all below in the next segment are functions used for hard difficulty gameplay.

def cpuHardChoice(stones): # function used for playing on hard difficulty
    global playerWins # " "
    global compWins # " "

    if stones != 0: # if stones is not equal to zero, the following algorithm will be enacted for computer choice
        quotient = stones % 4 # mods total number of stones by 4. In a range from 1-30, the quotient will always either be 0,1,2, or 3. Using these values one can determine ideal moves to be made.
        # ideal positions to pull down towards are on stone number 5, 9, 13, 17, 21, 25, 29 - algorithm ensures that when possible from any number in range 1-30, computer will pull to ideal position.
        # found this algorithm through analysing the question and trial and error.
        if quotient == 0: # if quotient is 0
            compChoice = 3 # comp choice is 3
            return compChoice # returns compChoice to be used in other cpu computation function
        elif quotient == 3: # " "
            compChoice = 2 # " "
            return compChoice # " "
        elif quotient == 2: # " "
            compChoice = 1 # " "
            return compChoice # " "
        elif quotient == 1: # " "
            compChoice = 1 # " "
            return compChoice #  " "

def cpuHard(stones): # identical to regular mode function, exlcuding compChoice processing, as that is executed in earlier function
    global playerWins
    global compWins
    compChoice = cpuHardChoice(stones)

    stones = stones - compChoice # uses calculated compChoice
    print("I have taken", compChoice, "from the pile. There now remains", stones, "left.")
    if stones == 0:
        print("You win!")
        playerWins += 1

        print("Player wins =", playerWins,"\n"
              "Computer wins =", compWins)

        replay= getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ")
        if replay == replay:
            getSpHard() # if replay is selected, will replay hard difficulty
    else:
        playerGameplayHard(stones) # if cpu does not lose on their turn, will call user to make their turn

def playerGameplayHard(stones): # identical to regular mode function, except it calls hard difficulty cpu choice, and will replay hard difficulty is hard is selected.
    global compWins
    global playerWins

    if stones > 0:
        stopper = False
        while not stopper:
            try:
                playerChoice = int(getInput("Select how many stones you would like to remove from the pile: ", "It seems you are a bit stuck. Enter a number between 1 and 3 to remove a desired amount of stones from the pile. Remember you can not purposely take the last stone from the pile!"))
                if playerChoice > stones or playerChoice not in range (1,4):
                    raise ValueError
                if stones == 3 and playerChoice == 3:
                    raise ValueError
                if stones == 2 and playerChoice == 2:
                    raise ValueError

                stopper = True
                break
            except (ValueError, TypeError):
                print("Error detected. Please reinput choice.")
                playerGameplayHard(stones)

        stones = stones - playerChoice
        print("You have taken", playerChoice, "from the pile. There now remains", stones, "left.")
        if stones == 0:
            print("You lose!")
            compWins += 1

            print("Player wins =", playerWins,"\n"
                  "Computer wins =", compWins)

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ")
            if replay == replay:
                getSpHard()
        else:
            cpuHard(stones)


def getSpHard(): # identical to regular mode function, except it calls hard difficulty for player gameplay and for cpu gameplay.
    print("\nSingle player Hard difficulty has been selected.\n"
          "Like I said before: good luck beating me!\n" 
          "Let's flip a coin to see who goes first. Heads it's you, tails it's me.")

    flipper = getInput("Press Enter to flip a coin ", "It seems you are a bit stuck. Press enter to flip a coin")

    if flipper == flipper:
        coinFlip = getHeadsorTails()
        stones = getStones()

    if coinFlip == "Heads":
        print("\nHeads! Okay, so you go first!")
        print("This game will be played with", stones,"stones")
        playerGameplayHard(stones)

    elif coinFlip == "Tails":
        print("\nTails! Okay, so I go first!")
        print("This game will be played with", stones,"stones")
        cpuHard(stones)

############################################################################################################################################################################################
# all below in the next segment are gameplay for the multiplayer mode.

def player1Gameplay(stones,player1,player2): # identical to older player gameplay functions. Except it users player names, different global variables for counting player wins, will replay multiplayer mode, and trades turns between each other rather than a computer.
    global player1Wins
    global player2Wins

    if stones > 0:
        stopper = False
        while not stopper:
            try:
                playerChoice = int(getInput(player1 + " ,Select how many stones you would like to remove from the pile: ", "It seems you are a bit stuck. Enter a number between 1 and 3 to remove a desired amount of stones from the pile. Remember you can not purposely take the last stone from the pile!"))
                if playerChoice > stones or playerChoice not in range (1,4):
                    raise ValueError
                if stones == 3 and playerChoice == 3:
                    raise ValueError
                if stones == 2 and playerChoice == 2:
                    raise ValueError

                stopper = True
                break
            except (ValueError, TypeError):
                print("Error detected. Please reinput choice.")
                player1Gameplay(stones,player1,player2) # calls itself if exceptions occur

        stones = stones - playerChoice
        print("You have taken", playerChoice, "from the pile. There now remains", stones, "left.")
        if stones == 0:
            print("You Lose!", player2, "wins!")
            player2Wins += 1 # differnce, player global variable annotation

            print(player1, "wins =", player1Wins,
                  player2, "wins =", player2Wins) # difference, annotates player scoreboard

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ")
            if replay == replay:
                multiplayerInit(player1,player2) # replays multiplayer if selected
        else:
            player2Gameplay(stones,player1,player2) # trades turns with other player function

def player2Gameplay(stones,player1,player2): # identical to first function, uses player 2 name instructiom.
    global player1Wins
    global player2Wins

    if stones > 0:
        stopper = False
        while not stopper:
            try:
                playerChoice = int(getInput(player2 + " ,Select how many stones you would like to remove from the pile: ", "It seems you are a bit stuck. Enter a number between 1 and 3 to remove a desired amount of stones from the pile. Remember you can not purposely take the last stone from the pile!"))
                if playerChoice > stones or playerChoice not in range (1,4):
                    raise ValueError
                if stones == 3 and playerChoice == 3:
                    raise ValueError
                if stones == 2 and playerChoice == 2:
                    raise ValueError

                stopper = True
                break
            except (ValueError, TypeError):
                print("Error detected. Please reinput choice.")
                player2Gameplay(stones,player1,player2) # " "

        stones = stones - playerChoice
        print("You have taken", playerChoice, "from the pile. There now remains", stones, "left.")
        if stones == 0:
            print("You lose!", player1, "wins!")
            player1Wins += 1 # ""

            print(player1, "wins =", player1Wins,
                  player2, "wins =", player2Wins) # ""

            replay = getInput("Do you want to play again? (yes/quit/help/main menu) ", "It seems you are a bit stuck. Type yes to play again, quit to end the game, or main menu to return to the main menu. ")
            if replay == replay:
                multiplayerInit(player1, player2) # ""
        else:
            player1Gameplay(stones,player1,player2) # ""
############################################################################################################################################################################################################
# Initilization and processing for muliplayer mode.

def getMultiplayer(): # multiplayer introduction
    print("\n"
          "Multiplayer has been selected.\n"
          "Welcome once more to the ancient game of Nim!") # introduces the multiplayer game mode

    checkIn = getInput("But before we begin, do you know how to play? (yes/no) ", "It seems like you're having some trouble. Type yes to continue or no to see the rules.") # check in for rules

    if checkIn == "no":
        print("No worries: take a look at the rules and come back after!")
        rulebook() # calls rulebook, like in single player

    print("\nSweet! Let's get started then!")
    player1 = getInput("\nWelcome Player One!, Please enter your name: ", "It seems you are a bit stuck, type in your name and press enter!") # asks for player1 name
    player2 = getInput("Welcome Player Two!, Please enter your name: ", "It seems you a bit stuck, type in your name and press enter!") # asks for player 2 name
    print("Welcome", player1, "and", player2,"to the game of nim!") # welcomes players

    multiplayerInit(player1, player2) # calls multiplayer iniatialization function
    return player1, player2 # returns player names.

def multiplayerInit(player1, player2): # takes the passing for player names
    iniation = getInput(player1 + " press enter to flip a coin so we can see who goes first. Heads you do. Tails player two does! ", "It seems you are a bit stuck. Press enter to flip a coin." )

    if iniation == iniation: # iniates game, gets coin flip and stones
        stones = getStones()
        coinFlip = getHeadsorTails()

    if coinFlip == "Heads": # player one goes first
        print("\nHeads! Okay, so " + player1 + " goes first!") # player 1 name is used
        print("This game will be played with", stones, "stones")
        player1Gameplay(stones,player1,player2) # calls player 1 gameplay

    elif coinFlip == "Tails": # player two goes first
        print("\nTails! Okay, so " + player2 +  " goes first!") # player 2 name is used
        print("This game will be played with", stones, "stones")
        player2Gameplay(stones,player1,player2) # calls player 2 gameplay
##############################################################################################################################################################################################################

name = introduction() # initializes introduction, so name variable can be used thoughout entire program
mainMenu() # runs main menu function as the basis of all gameplay. Everything functions through infinite loops. Exiting throught the main menu, or quitting manually throughoutt the getInput function is necessary.