# wrt p program using function to find greaterest of three numbers.

# a =45
# b =58
# c=856
def  greater():
    if( a>b and c>a):
        return a
    elif(b>c and b>a):
        return b
    elif (c>a and c>b):
        return c
    
a =45
b =58
c =8
print(greatest(a,b,c))