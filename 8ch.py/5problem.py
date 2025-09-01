#wrt a python function to print first n line of the folloeing pattern.
# ***
# **
# *
# for n =3

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(3)

    