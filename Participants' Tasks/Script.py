#auhtor: Ahmed Mohamed
#description: simple guessing game
#org: K-Vector

#includes

from random import randint

#functions

def firstStage():
    trials = 3      # can be changed
    while(True):
        inputString = input("Enter your Word: ")
        if(inputString != "KVector"):
            trials = trials - 1
        if(inputString == "KVector"):
            print("Congrats!, you made it up to the next stage")
            return
        if(trials == 0):
            print("Game Over!")
            exit()

def secondStage():
    # ask for the lower and upper integer numbwr bounds
    lowerBound = int(input("Enter a lower bound to guess: "))
    upperBound = int(input("Enter an upper bound to guess: "))
    # generate the number for play
    correctNumber = randint(lowerBound, upperBound)
    #empty list for the attempts of the player
    InputNumbers = []

    while(True):
        #ask for guess number
        # print("enter a number between "+ str(lowerBound) + " and "+ str(upperBound) + ": ")
        inputNumber = int(input("enter a number between "+ str(lowerBound) + " and "+ str(upperBound) + ": "))
        #add it to the attempts list
        InputNumbers.append(inputNumber)
        #respond to the user
        if(inputNumber > correctNumber):
            print("you entered a too large number")
        if(inputNumber < correctNumber):
            print("you entered a too little number")
        if(inputNumber == correctNumber):
            print("Congrats!, you guessed the right number after "+ str(len(InputNumbers))+" times")
            print("here's a list of your attempts")
            print(InputNumbers)
            break

    response = input("Do you want to continue? y/n: ")
    if(response == 'n'):
        print("Thanks for Playing!")
        exit()


#main application code

while(True):
    firstStage()
    secondStage()
