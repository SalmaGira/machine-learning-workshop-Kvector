from random import randint

word = "KVector"
trials_num = 3
win= False
while trials_num>0 and not win:
  guess_word = input("Enter your word: ")
  if word != guess_word:
    trials_num -=1
  else:
    win = True

if not win:
  print("Oh! You lost")
else:
  print("Congrats! You made it to the next stage!")
  again = True
  while again:
    lower = int(input("Enter a lower bound to guess: "))
    upper = int(input("Enter an upper bound to guess: "))
    random_num = randint(lower,upper)
    guess_num = int(input("Enter a number between {} and {}: ".format(lower,upper)))
    trials=[]
    while guess_num != random_num:
      trials.append(guess_num)
      if guess_num > random_num:
        print("You entered a too large number")
      else:
        print("You entered a too small number")
      guess_num = int(input("Enter a number between {} and {}: ".format(lower,upper)))
    print("Congrats! You guessed the number after {} times".format(len(trials)))
    print("Here's the list of your attempts")
    print(trials)
    again = True if input("Do you want to play again? y/n: ") == "y" else False
    if not again:
      print("Thanks for playing!")
