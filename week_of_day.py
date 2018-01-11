# input : 3
# output : Tue
# user_input = int(input("enter a number between 1 to 7:"))
# day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# for num,day in enumerate(day_list,1):
#     if user_input == num:
#         print(f"{num} = {day}")
#         break
# else:
#     print("wrong input")

# user_input = int(input("enter a number between 1 to 7:"))
# day_list = {1:'sunday',2:'monday',3:'tuesday',4:'wednesday',5:'thursday',6:'friday',7:'saturday'}
# for num,day in day_list.items():
#     if user_input == num:
#         print(f"{num} = {day}")
#         break
# else:
#     print("wrong input")
user_input = int(input("enter a number between 0 to 6:"))
day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
if user_input < 0 or user_input > 6:
    print("invalid input")
else:
    print(f"{user_input} means {day_list[user_input]}")





