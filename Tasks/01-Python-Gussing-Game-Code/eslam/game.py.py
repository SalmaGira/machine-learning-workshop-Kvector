import random

bool=False
x=("kvector",'Kvector','KVECTOR')

print ('hello sir')
for n in range (1,4):
    aut=str(input ("enter your word,please:"))
    if aut in x:
        bool=True  
        break 
    else :
        print("not right!")
        print ("you have",3-n,"attemps")
if bool == False :
    print ("oh!You lose")
else:
    print ("graet! You made it to the next round")    
'''
# i made it for follish people like me who enter quick without reading carefully but there's an error  
entered1=int (input("choose a lower bound to guess:")) 
entered2=int (input("choose an upper bound to guess:")) 
if entered1>entered2:
    b2=entered1
    b1=entered2
else:
    b1=entered1
    b2=entered2
 '''
while(bool==True):    
    b1=int (input("choose a lower bound to guess:")) 
    b2=int (input("choose an upper bound to guess:"))    
    
    selected=random.randint(b1,b2)
    
        
    entered=input("enter your guess between "+str(b1)+" and "+str(b2)+":")
    while(1):  
        
        if entered.isdigit() == False:
                entered=input ('please,enter a number')
        else :
            break
    while(1):
        
        if int (entered) not in range(b1,b2):
                    entered=input( ("enter a number between boundries you entered before:"))
        else:
            break 
    l1=[]    
    n=0      
    while (1):
        n+=1
        l1.append(entered)
        if int(entered)>selected:
           entered=input( ('you entered too large value!'))
        elif int (entered)<selected:
            entered=input( ('you entered a too small value!'))
        else:
            break         
    
    print ('Yes!You Win after',n,"times")
    print("Here's a list of your attamps!")
    print(l1)
    q=input("you want to play again y/n:")
    if q=="n" :
        print("Thanks for playing!")
        break
     






      
 











'''

if b1>b2:
    for n in range (b2,b1+1):
         l1.append(n)
else:
    for n in range (b1,b2+1):
       l1.append(n)
print(l1)

'''