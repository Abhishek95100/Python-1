a = int(input("Enter your age:"))
# if statement 1
if(a%2==0):
    print("a is even")

# End of if statement 1
#if statement 2
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age"
    )

else:
    print("you are below the age of consent")
    
# End of if statement 2

print("end of program")