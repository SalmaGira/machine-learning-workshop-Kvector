import random


def checkpassword ():
    for _ in range(3):
        if "kvector" == input("Enter your word: "):
            return True
    return False

def console():
    while True:
        if checkpassword():
            lower = int(input("Congrats! You made it to the next stage!\nEnter a lower bound to guess: "))
            upper = int (input("Enter an upper bound to guess: "))
            myrandom = random.randint(lower,upper)
            guess = lower - 1
            attempts = []
            while guess != myrandom:
                if attempts != []:
                    print("You entered too {} number".format("large" if guess > myrandom else "small"))
                guess = int(input("Enter a number between {} and {}: ".format(lower,upper)))
                attempts.append(guess)
            print("Congrats! You guessed the right number after "+str(len(attempts))+" times\nHere's the list of your attempts\n",attempts)
            if input("Do you want to continue? y/n: ") != "y":
                break
        else:
            print("Oh you lost!")
            break

if __name__ == "__main__":
    console()