print("1 for addition")
print("2 for multiplication")
print("0 for exit")
input_list = (input("enter your elements:")).split(" ")
input_num = int(input("enter your choice:"))
while input_num == 1:
    sum = 0
    for item in input_list:
        sum = sum+ int(item)
    print(sum)
    input_num = int(input("enter your choice:"))
while input_num == 2:
    mult = 1
    for item in input_list:
        mult = mult * int(item)
    print(mult)
    input_num = int(input("enter your choice:"))
if input_num == 0:
    print("exit")
else:
    print("you have entered an wrong input")