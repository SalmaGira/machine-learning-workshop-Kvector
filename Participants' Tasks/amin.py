import random
def guessGame():
    secret_word = "K VECTOR"
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = input("Enter your word: ")
        guess_count += 1
        if guess == secret_word:
            print ("congrats you made it to the next step")
            break
        elif guess_count == guess_limit:
            print("oh you lost")
            quit()
    lower = int(input("Enter a lower bound to guess: "))
    upper = int(input("Enter upper bound to guess: "))
    x = random.randint(lower, upper)
    guess_count = 0
    List = []
    while True:
        user_guess = int(input(f"Enter a number between {lower} and {upper}: "))
        guess_count += 1
        List.append(user_guess)
        if user_guess < x:
            print("You entered a too small number ")
        elif user_guess > x:
            print("You entered too large number")
        else:
            print(f"Congrats! You guessed the right number after {guess_count} times")
            print('Here is the list of your attempts')
            print(List)
            return

guessGame()

play_again = input('Do you want to play again y/n')
if play_again == 'y'.lower():
    print ("let's play again")
    guessGame()

else:
    print("thanks for playing")
    exit()