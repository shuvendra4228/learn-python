# input : 33
# output : Thur
input_num = int(input("enter a number :"))
user_input = input_num % 7
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
if input_num < 0:
    print("invalid input")
else:
    print(f"{input_num} = {days[user_input]}")