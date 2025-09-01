# Write a program to find out whether a student
# is pass bro' fail if it regires total 40% and
# st least 33), in each subject to pass. Asune
# 3 Sulyects and take morks as an input from the user

marks1 = int(input("Enter marks1:"))
marks2 = int(input("Enter marks2:"))
marks3 = int(input("Enter marks3:"))
marks4 = int(input("Enter marks4:"))

#check for total percentage

total_percentag = (100*(marks1 + marks2 +marks3 +marks4))/400

if(total_percentag>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("you are pass",total_percentag)

else:
    print("you failed,try again next yera!",total_percentag)


