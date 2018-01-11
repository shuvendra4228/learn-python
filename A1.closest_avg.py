input_list = [int(x) for x in input("enter a list :").split(" ")]
sum = 0
for num in input_list:
    sum += num
avg = sum/len(input_list)
diff,key = 0, 0
temp = abs(avg-(input_list[0]))
for index in range(1,len(input_list)):
    diff = abs(avg- input_list[index])
    if diff < temp:
        temp = diff
        key = index
print(f'closest number of {avg} is {input_list[key]}')

