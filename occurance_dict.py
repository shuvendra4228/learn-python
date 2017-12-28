dict = {}
str = "cuttack"
for i in str:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
max = 0
k = 0
for key,value in dict.items():
    if value >= max:
        max = value
        k = key
        print(k ,":", max)