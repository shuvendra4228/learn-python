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
for k,v in dict.items():
    if v >= max:
        max = v
        key = k
        flag = 1
        print("{} has a occurance of {} times".format(key,max))
    
else:
    print("no highest ocuurance of any word")


