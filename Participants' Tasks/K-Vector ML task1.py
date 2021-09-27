
# This is a guess the number game and such
# It has two rounds where you guess a secret word in the first and a secret number in the second
# Sounds fun, right?


# no

from random import randint
from time import sleep

def round1():
    for i in range(3):
        secretWord = input('Enter the secret word: ')
        if secretWord.lower() == 'k vector':
            print('Congrats! You made it to the next stage!\n')
            return True
        else:
            print('WRONG! ',end='')

def round2_get_bounds():
    while True:
        try:
            lowBoundary = int(input('Enter a lower bound for the number: '))
            break
        except ValueError:
            print('THAT\'S NOT A NUMBER, DUMMY!!!')
    while True:
        try:
            highBoundary = int(input('Enter an upper bound for the number: '))
            if highBoundary <= lowBoundary:
                print('Dum Dum, the upper bound can\'t be less than or equal to the lower bound! Try Again!')
            else:
                break
        except ValueError:
            print('THAT\'S NOT A NUMBER, DUMMY!!!')
    return highBoundary, lowBoundary

def round2_check_num(bigNumber, smolNumber, coolNumber):
    ansList = []
    while True:
        while True:
            try:
                print('\nEnter a number between ', smolNumber, ' and ', bigNumber, ': ', end='')
                answer = int(input())
            except ValueError:
                print('bro, what? -__-')
                continue
            if smolNumber > answer or bigNumber < answer:
                print('brother, please enter a number between the bounds') 
            else:
                break
        ansList.append(answer)
        if answer == coolNumber:
            return ansList
        elif answer < coolNumber:
            print('Nooooo! the secret number is bigger')
        elif answer > coolNumber:
            print('Nooooo! the secret number is smaller')


def main():
    print('hello human, I have come to take over your planet',end='')
    sleep(3.5)
    print('\n\nJust kidding, this is just a lame guess the number game\nPlease have fun and don\'t die')

    while True:
        if round1():
            upperBound, lowerBound = round2_get_bounds()
            secretNum = randint(lowerBound, upperBound)
            finalList = round2_check_num(upperBound, lowerBound, secretNum)
            
            if len(finalList) == 1:
                print('WHAT A DAMN LEGEND!!! You found the Number in 1 try!')
            else:
                print('Congratulations mate, you found the number in ', len(finalList), 'tries!!!')
                print('Here\'s a list of your attempts:')
                print(finalList)
        else:
            print('You lost suckahhh!')
        
        retry = input('Do you want to play again? y/n \n')
        if retry.lower() not in ('yes', 'y'):
            print('okay whatever, Im leaving')
            break

if __name__ == "__main__":
    main()

# I should have wrote comments but I didn't