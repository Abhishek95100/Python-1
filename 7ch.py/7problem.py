# Write a program to pprint the following star pettern
'''*
 ** 
  ***** for n=3'''

n = int (input("Enter number:"))
for i in range(1,n+1):
    print("*"(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

