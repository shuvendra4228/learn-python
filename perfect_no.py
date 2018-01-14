input_num = int(input('enter a number: '))
sum = 0
for item in range(1,input_num):
    if input_num % item == 0:
        sum += item
if sum == input_num:
    print(f"{input_num} is a perfect_number")
else:
    print("not a perfect_number")