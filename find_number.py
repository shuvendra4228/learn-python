lst = [int(num) for num in input("enter your numbers separated by commas: ").split(",")]
input = int(input("enter a number:"))
flag = False
for number in lst:
    if input == number:
        print("number found")
        flag = True
        break
if not flag:
    print("not found")