str = input("enter a string:")
letter = input("enter a letter:")
n = len(str)
i = 0
count = 0
while i < n:
    pos = str.find(letter,i,n)
    if pos != -1:
        print(pos+1)
        i = pos+1
        count += 1
    else:
        break
print(count)




    
        




