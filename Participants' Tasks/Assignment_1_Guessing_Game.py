from random import *


def guessing_game():
    while True:
        try:
            lower = int(input("Enter a lower bound to guess: "))
            upper = int(input("Enter an upper bound to guess: "))
            if lower >= upper:
                print("Lower bound should be smaller that upper boundry!")
                continue
        except:
            print("Please, Enter integer boundaries!")
            continue
        break
    lucky = randrange(lower, upper)
    answer = lucky + 1
    counter = 0
    attempts = list()
    while int(answer) != lucky:
        answer = input("Enter a number between {} and {}: ".format(lower, upper))
        try:
            answer = int(answer)
        except:
            answer = lucky + 1
            print("Please, Enter an integer number!")
            continue
        
        if answer < lower or answer > upper:
            print("You entered a number out of range!")
            continue
        else:
            counter += 1
            attempts.append(answer)
            if answer > lucky:
                print("You entered a too large number!")
                continue
            elif answer < lucky:
                print("You entered a too small number!")
                continue
    print("Congrats, You guessed the right number after {} times!".format(counter))
    print("Here's the list of your attempts")
    print(attempts)
    return True


password = input("Enter your word:")
count = 1
while password.lower() != "kvector":
    if count == 3:
        print("Oh! You lost.")
        exit()
    else:
        password = input("Enter your word:")
        count += 1
        

print("Congrats! You made it to the next stage!")
check = guessing_game()
while check:
    answer = input("Do you want to continue? y/n: ")
    if answer.lower() == "y":
        check = guessing_game()
        continue
    elif answer.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I can't understand.")
        continue
