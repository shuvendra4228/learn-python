email = input("enter your email: ")
str1= email.split("@")
str2 = str1[1].split(".")
str2.append(str1[0])
if len(str2) == 3:
    print("valid email")
else:
    print("not valid")

