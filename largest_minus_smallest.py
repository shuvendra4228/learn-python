# input : [1, 3 , 4, 6 , 7, 9]
# output : 9-1 = 8
input_list = [int(x) for x in input("enter a list of number separated by space: ").split(" ")]
max = input_list[0]
min = input_list[0]
for i in range(1,len(input_list)):
    if input_list[i] > max:
        max = input_list[i]
    elif input_list[i] < min:
        min = input_list[i]
print(f"{max} - {min}= {max - min}")
    
