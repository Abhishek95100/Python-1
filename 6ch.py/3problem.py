# A spam comment is definded as a text containsing
# foflowing Reywords:
# make a lot of money, buy now, I
# now sulycribe this
# "click this" Write a propram to deteet these spams

p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("Enter your comment:")

if((p1 in message)or (p2 in message )or(p3 in message)or (p4 in message)):
    print("this comment is a spam")

else:
    print("this comment is not a spam")