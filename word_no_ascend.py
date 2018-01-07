# input : dbca412
# ouput : 124abcd
str_alpha = ''
str_numb = ''
input_str = input("enter an input:")
for char in input_str:
    if char.isdigit():
        str_numb += char
    elif char.isalpha():
        str_alpha += char
newstr = sorted(str_alpha) + sorted(str_numb)
print("".join(newstr))



    

    

