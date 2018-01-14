armstr = int(input("enter a number: "))
temp = armstr
sum = 0
while temp > 0:
    reminder = temp%10
    sum = sum + reminder**3
    temp = temp//10
if armstr == sum:
    print(f"{armstr} is a armstrong number:")
else:
    print("not a armstrong number")
