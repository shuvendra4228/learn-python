email = input("enter your email: ")
array_1 = email.split("@")

if len(array_1) == 2:
    array_2 = array_1[1].split(".")
    if len(array_2) == 2 and len(array_2[0]) != 0:
        print("email is valid")
    else:
        print("not valid")
else:
    print("not a valid email")