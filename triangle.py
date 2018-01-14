input_row = int(input("enter number of rows: "))
num = 0
for i in range(input_row, 0, -1):
    print(" "*num,end =" ")
    print("* "*i)
    num = num +1

