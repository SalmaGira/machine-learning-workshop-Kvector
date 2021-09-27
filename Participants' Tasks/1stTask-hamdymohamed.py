import random as rn
password = 'KVector'
for num in range(1 , 4):
    x = input('Enter your word:    ')
    if x == password:
        print('Congrats! You made it to the next stage')
        break
    if num == 3 and x != password:
        print('Oh! You lost')
lw = int(input('Enter a lower bound to guess:   '))
up = int(input('Enter an upper bound to guess:  '))
list1 = list(range(lw,up+1))
x = rn.choice(list1)
list2 = []
for n in range(up+1-lw):
    y = int(input('Enter a number between {} and {}:  '.format(lw,up)))
    if y == x :
        break
    elif y < x :
        print('You Entered a too small number')
        list2.append(y)
    else :
        print('You Entered a too large number')
        list2.append(y)
print('Congrates! You gussed the right number after {} Times'.format(n))
print('Here is a list of your attempts')
print(list2)
f = input('Do you want to continue?  y/n:   ')
if f == 'y':
   f = 1
else:
    f = 0
    print('Thanks for playing!')
while f == 1:
    lw = int(input('Enter a lower bound to guess:   '))
    up = int(input('Enter an upper bound to guess:  '))
    list1 = list(range(lw,up+1))
    x = rn.choice(list1)
    list2 = []
    for n in range(up+1-lw):
        y = int(input('Enter a number between {} and {}:  '.format(lw,up)))
        if y == x :
           break
        elif y < x :
           print('You Entered a too small number')
           list2.append(y)
        else :
           print('You Entered a too large number')
           list2.append(y)
    print('Congrates! You gussed the right number after {} Times'.format(n))
    print('Here is a list of your attempts')
    print(list2)
    f = input('Do you want to continue?  y/n:   ')
    if f == 'y':
       f = 1
    else:
       f = 0
       print('Thanks for playing!')
