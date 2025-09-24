# 1 से 100 तक के odd numbers का sum निकालो।

sum_odd=0
for i in range(1,101):
    if i % 2 != 0:
        sum_odd +=i
print("1 to 100 odd number sum=",sum_odd)
