def guess(value):
    test=True
    j=0
    while test:
        if value>upper_bound or value<lower_bound:
            value=input('You entered an out of range number:')
            value=int(value)
        elif value>number:
            list1.append(value)
            value=input('You entered a too large number:')
            value=int(value)
            j+=1
        elif value<number:
            list1.append(value)
            value=input('You entered a too small number:')
            value=int(value)
            j+=1
        elif value==number:
            list1.append(value)
            j+=1
            print('Congrats! You guessed the right number after {0} times'.format(j))
            test=False

turns=0
i=0
list1=[]
while i<3:
    key_word=input('Enter you word:')
    if key_word == 'kvector':
        print('Congrats! You made it to the next stage!')
        break
    else:
        i+=1
if i==3:
    print('oh! You lost')
    quit()
while turns<10:
    lower_bound=input('Enter a lower bound to guess:')
    upper_bound=input('Enter an upper bound to guess:')
    lower_bound=int(lower_bound)
    upper_bound=int(upper_bound)
    import random
    number= random.randrange(lower_bound,upper_bound)
    inp='Enter a number between {0} and {1} :'.format(lower_bound,upper_bound)
    value=input(inp)
    try :
        value=int(value)
    except:
        value=('Please enter an integer number:')
        value=int(value)
    guess(value)
    print("Here's the list of ypur attempts")
    print(list1)
    play_again=input('Do ypu want to continue? y/n:')
    if play_again=='y':
        continue
    elif play_again=='n':
        turns=11
print('Thanks for playing!')
quit()
