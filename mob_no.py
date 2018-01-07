mob_input = input("enter your mobile number:")
if len(mob_input) == 10 and mob_input[0] == '9':
    print("mobile is valid")
elif len(mob_input) == 11 and mob_input[0] == '0':
    print("mobile number is a valid number")
elif len(mob_input) == 13 and mob_input[0:3] == '+91':
    print("valid mobile number")
else:
    print("invalid number")

