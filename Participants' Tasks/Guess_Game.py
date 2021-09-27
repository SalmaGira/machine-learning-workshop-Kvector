import random
secert_word="kvector"


def round1() :
    trials=1
    while trials< 4 :
        input_word=input("Enter your word : ")
        if input_word==secert_word :
            print ("Congerts! You made it to the next stage!")
            return "true"
            break
        if trials == 3:
            print ("Oh! You lost")
            return "false"
            break
        trials +=1

    

def again():
    decision=input("Do you want to continue? y/n: ")
    if decision=="y" :
        round2()
    else :
        print("Thanks for playing!")     
     
def round2() :
    try :
        lower_bound=input("Enter a lower bound to guess: ")
        a=int(lower_bound)
    except :
        a=(input("Please enter a lower number as lower bound: "))
        
    
    try :
        large_bound=input("Enter an upper bound to guess: ")
        b=int(large_bound)
       
        
    except :
        b=(input("Please enter an integer number as upper bound: "))
        

    random_num= random.randint(a,b)
    #print(random_num)#this code help me in the test

    try :
        input_num=input("Enter a number between "+lower_bound +" and "+large_bound+": ")
        input_num=int(input_num)
    except :
       input_num=(input("Please enter an integer number: "))
       
       input_num=int(input_num)

    attempts=[]

    while input_num != random_num :
        attempts.append(input_num)
        if input_num > random_num and input_num >=a and input_num <=b :
            print ("You entered a too large number")
            try :
                input_num=input("Enter a number between "+lower_bound +" and "+large_bound+": ")
                input_num=int(input_num)
            except :
                input_num=(input("Please enter an integer number: "))

        elif input_num < random_num and input_num >=a and input_num <=b :
            print ("You entered a too small number")
            try :
                input_num=input("Enter a number between "+lower_bound +" and "+large_bound+": ")
                input_num=int(input_num)
            except :
                input_num=(input("Please enter an integer number: "))

        else :
            try :
                input_num=input("You entred an out of range number: " )
                input_num=int(input_num)
            except :
                input_num=(input("Please enter an integer number: "))

            
    
    attempts.append(input_num)
    
    print("Congerts! You gussed the right number after "+str(len(attempts))+" times") 
    print("Here is the list of your attempts")
    print(attempts)
    again()



                   
def game():
    if round1()=="true":
       round2()

    
        
game()
    

    
