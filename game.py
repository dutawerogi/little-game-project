import random
 
# Setup game variabels
randomNumber = 10 #random.randint(1,100)
print(randomNumber)
gameRunning = True
numbersGuessed = []
tries = 0
 
# Game startup
print("Hello, and welcome to this simple console game.")
playerName = input("What is your name? ")
print("Hello, " + playerName)
print("Ok, so we're going to play a guessing game today.")
print("Please guess a number between 1 - 100")
print("----------------------------------------")
print("-If you need help on the way, type HELP-")
print("----------------------------------------")
 
# Game loop
while gameRunning :
 
    # Getting input from user (number or help command)
    guessNumber = input("Guess a number: ")
 
    # HELP command
    if guessNumber == "HELP":
        print("You can use the following commands:")
        print("[HELP] (Displayed help commands)")
        print("[NUMBERS] (Displayed already gussed numbers)")
        continue
 
    # NUMBERS command
    if guessNumber == "NUMBERS":
        if len(numbersGuessed) > 0:
            i = 0
            for number in numbersGuessed:
                i += 1
                print("%s) %s" % (i, number))
        else:
            print("No numbers has been guessed yet.")
        continue
 
    # Add guessed number to list
    numbersGuessed.append(guessNumber)
 
    # Keeping tack of the number of attempts the user has
    tries += 1
 
    # If the number was correct
    if int(guessNumber) == randomNumber:
 
        print("You got the correct number after " + str(tries) + " attempts.")
        print("These are the numbers you tried to guess:")
 
        # Print out all guessed numbers
        for number in numbersGuessed:
            print(number)
 
        # Stop the while loop from running
        gameRunning = False
 
    elif int(guessNumber) < randomNumber:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
