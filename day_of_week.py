# input : 33
# output : Thur
input_num = int(input("enter a number :"))
user_input = input_num % 7
day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
if input_num < 0:
    print("invalid input")
else:
    for num,day in enumerate(day_list,0):
        if user_input == num:
            print(f"{num} = {day}")
            break


