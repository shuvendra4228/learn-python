mob_input = input("enter your mobile number:")
if len(mob_input) == 10 and mob_input[0] == '9':
    print("mobile number is valid")
elif len(mob_input) == 11 and mob_input[0] == '0':
    print("mobile number is valid")
elif len(mob_input) == 13 and mob_input[0:3] == '+91':
    print("mobile number is valid")
else:
    print("invalid mobile number")