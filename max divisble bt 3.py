lst = [5,6,9,13,1,12,15,16,17,20,21,23,25]
max = 0
Flag = False
for i in lst:
    if i > max and i%3 == 0  :
        max = i
        Flag = True
print(max,"is largest")
if Flag == False:
    print("no such element:") 