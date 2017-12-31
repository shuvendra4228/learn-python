input_str = ("biki is a good biki programmer good")
lst = input_str.split(" ")
dict = {}
max = 1
for item in lst:
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1
        if dict[item] > max:
            max = dict[item]

print(dict)

if max == 1 :
    print("There is no item with one highest occurance")
else :
    for k, v in dict.items():
        if v == max:
            print(f"Highest occurance of {k} is {v}")