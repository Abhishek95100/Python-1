# rite a program to find whether a given number
# is prime or not

n =int(input("Enter number:"))

for i in range(2,n):
    if(0==n%i):
        print("Not a prime number")
        break
else:
    print("prime number")