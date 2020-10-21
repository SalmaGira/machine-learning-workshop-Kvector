#p2:print()-input()
name = input("Whats ur name: ")
print ("hello",name)

#p3:vars-indentation
i = 0
while i<4:
    print(i)
    i = i+1

#p5:datatypes-casting
n1 = input("enter the first number:")
n2 = input("enter the second number:")
print(int(n1)+int(n2))

#p6:arithmetics
num1 = int(input("enter the smaller number:"))
num2 = int(input("enter the larger number:"))
print(num2%num1)

#p9:conditionals
no1 = int(input("enter number:"))
no2 = int(input("enter number:"))
no3 = int(input("enter number:"))
print(no1>no2>no3)

#p11:control_flow:while-in
registered_names = ["ahmed","ali","maha","yousif","zakaria"]
guest = input("Enter Your Name: ")
while True:
	if guest in registered_names :
		print("Welcome",guest)
	else :
		print("sorry, you are not registered")

#p12:control_flow:if-else
noo1=int(input("enter the first number:"))
noo2=int(input("enter the second number:"))
if noo1>noo2:
    print("the first number is larger")
elif noo2>noo1:
    print("the second number is larger")
else:
    print("they are equal")

#p13:control_flow:break-continue
ite = 0
while True:
    ite+=1
    if(ite==13):
        break
    if(ite%3):
        continue
    print(ite)

#p14:control_flow:for-loopy_else
for z in range(10):
    print(z)
    if z==9: #change to 11 to see else invoking 
        break
else:
    print("else invoked")

#p18:functions
def reverse_my_name(myname):
    reversing_list = []
    i=0
    while i<len(myname):
        reversing_list += myname[len(myname)-i-1]
        i+=1
    reversed_string = "".join(reversing_list)
    return reversed_string