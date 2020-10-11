import random

def game():
    lower = int(input("Enter a lower bound to guess: "))
    upper = int(input("Enter an upper bound to guess: "))
    rand = random.randint(lower,upper)
    attempts = []
    num = int(input("Enter a number between "+str(lower)+" and "+str(upper)+": "))
    while True:
        attempts.append(num)
        if num == rand:
            print("Congrats! You guessed the right number after "+str(len(attempts))+" times\nHere's the list of your attempts\n", attempts)
            if input("Do you want to continue? y/n: ") == "y":
                game()
                return
            else:
                return
        else:
            if num>rand :
                print("You entered a too large number")
            else :
                print("You entered a too small number")
            num = int(input("Enter a number between "+str(lower)+" and "+str(upper)+": "))

def main():
    for i in range (3):
        if input("Enter your word: ").lower() == "kvector":
            print("congrats! You made to the next stage!")
            game()
            break
        if i == 2:
            print("Oh You Lost")



if __name__ == "__main__":
    main()