# wrt a python function to remove a given word form a list an strip it at the same time.

def remove(A,word):
    n =[]
    for item in A :
        if not (item == word):
            A.append(item.strip(word))
            return A
    for item in A:
       A.remove(word)
       return A
         
 
A = ["apple","banana","grape","orange","an"]

print(remove(A,"an"))

