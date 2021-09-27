import random
def replay():
 secret_word= 'K VECTOR'
 Guess_number= 0
 Guess_limit= 3
 while Guess_number < Guess_limit:
      name = input ("Enter your word : ")
      Guess_number +=1
      if name == secret_word:
          print("Congrats, you up to the higher level" )
          break
      elif Guess_number == Guess_limit:
          print("OH! YOU LOST")
          quit()

 numofguesses=0
 print("Enter your lower bound to a guess: ")
 A=input()
 A=int(A)
 print("Enter your upper bound to a guess: ")
 B=input()
 B=int(B)
 number = random.randint(A,B)
 print(f"Enter a number between {A} and {B}")
 guess_no = input()
 guess_no = int(guess_no)
 attempts = []
 while  guess_no != number:
     attempts.append(guess_no)
     if guess_no < number:
         print("Number is too low " )
         print(f"Enter a number between {A} and {B}")
         guess_no = input()
         guess_no = int(guess_no)
         numofguesses += 1
     elif guess_no > number:
         print("Number is too high ")
         print(f"Enter a number between {A} and {B}")
         guess_no = input()
         guess_no = int(guess_no)
         numofguesses += 1
     if guess_no == number:
         break
 if guess_no == number:
     numofguesses += 1
     numofguesses= str(numofguesses)
     print(f"Congrats! you guessed the right number after {numofguesses}  times")

 print("Here's the list of your attempts")
 attempts.append(guess_no)
 print(attempts)

replay()
while True:
    answer = input('Do you want to continue?' 'y/n' + ':')
    if answer.lower() =='y':
        print("let's play again")

    else:
        print("Thanks for playing!")
        exit()
    replay()
