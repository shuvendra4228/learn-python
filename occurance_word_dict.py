input_str = ("biki is a good programmer")
lst = input_str.split(" ")
dict = {}
for item in lst:
    if item not in dict.keys():
        dict[item] = 1
    else:
        dict[item] += 1
print(dict)
max = 0
key = 0
if len(set(dict.values())) == 1:
    print("no highest occurance:")
else:
    for k,v in dict.items():
        if v > max:
            max = v
            key = k
            print(key,":",max)    


