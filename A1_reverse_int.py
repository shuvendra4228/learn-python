temp = int(input("enter a number:"))
temp1 = temp
rev = 0
while temp1 > 0:
    reminder = temp1 % 10
    temp1 = temp1//10 
    rev = rev*10 + reminder
print(f"reverse of {temp} is {rev}")