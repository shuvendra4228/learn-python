temp = int(input("enter a number:"))
rev = 0
while temp > 0:
    reminder = temp % 10
    temp = temp//10 
    rev = rev*10 + reminder
print(rev)


