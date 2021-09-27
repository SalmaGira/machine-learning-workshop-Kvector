from random import randrange

def check(num):
    while (num.isdigit() == False):
        num = input("please enter a positive integer: ")
    return(num)

def enter_an_answer(answer,lower,upper,right_answer):
    answer.append(input("enter a number between {} and {} :".format(lower,upper)))
    answer[-1] = int(check(answer[-1]))
    
    is_right(answer,right_answer,len(answer))
    
    if (answer[-1] < right_answer):
        print("you entered a too small number")
        enter_an_answer(answer,lower,upper,right_answer)
    
    if (answer[-1] > right_answer):
        print("you entered a too large number")
        enter_an_answer(answer,lower,upper,right_answer)
        
def is_right(Ans,RightAns,tries):
    if (Ans[-1] == RightAns):
        print("Congrats you knew the right number after {} times".format(tries))
        print("These are your attempts {}".format(Ans))
        q = input("do you want to continue ? y/n: ")
        if (q == 'y'):
            next_stage()
        else:
            print("Thank you for playing")
    


lost = False
for i in range(3):
    key = input ("Enter your word: ")
    if (key.isdigit() == False and key == "KVector" ):
        print("Congrats you made it to the next stage !")
        break
    else:
        if (i == 2):
            print("You lost")
            lost = True
def next_stage():
    lower = input("enter a lower bound: ")
    lower = int(check(lower))
    
    upper = input("enter an upper bound: ")
    upper = int(check(upper))
    
    right_answer = randrange(lower,upper)
    
    answer =[]
    enter_an_answer(answer,lower,upper,right_answer)
    

if (lost == False):
    next_stage()
