array = [int(x) for x in input("enter a list :").split(" ")]
max = 0
for num in array:
    if num > max:
        max = num
print(max)
second_max = 0
for num1 in array:
    if num1 > second_max and num1 < max:
        second_max = num1 
print(second_max)
third_max = 0
for num2 in array:
    if num2 > third_max and num2 < second_max:
        third_max = num2
print(third_max)
fourth_max = 0
for num3 in array:
    if num3 > fourth_max and num3 < third_max:
        fourth_max = num3
print(fourth_max)
fifth_max = 0
for num4 in array:
    if num4 > fifth_max and num4 < fourth_max:
        fifth_max = num4
print(fifth_max)
