list_input1 = [1,2,3,4,5,6,7]
list_input2 = [3,4,5,6,7,8,9,10]
list_input3 = []
for item in list_input1:
    for num in list_input2:
        if item == num:
            list_input3.append(item)
print(list_input3)