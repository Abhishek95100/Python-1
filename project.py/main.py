# we all have played snake water gun game in our childhood.if you haven't ,google the rule of this game write a python program capable of playing this game with the user.

import random
'''
 1 for snake
-1 for water
 0 for gun


'''
computer = random.choice([-1,0,1])

youstr = int(input("Enter your choice:"))
youDict ={"s":1,"W":-1,"g":0}
reversedict ={1:"snake",-1:"water",0:"gun"}

you = youDict [youstr] 

# by now we have computer (variable),you and computer
print(f"you chose{reversedict[you]}\ncomputer chose {reversedict[computer]}")

print()

if (computer == you):
    print("its a draw")

else:
    if (computer ==-1 and you ==1):
        print("you win!")

    elif(computer ==-1 and you ==0):
        print("you lose!")

    elif(computer ==1 and you ==-1):
        print("you lose!")

    elif(computer ==1 and you ==0):
        print("you win!")

    elif(computer ==0 and you ==-1):
        print("you win!")

    elif(computer ==0 and you ==1):
        print("you lose!") 

    else:
        print("something went wrong")  