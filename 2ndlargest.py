lst = [9,2,3,4,5,6,7]
max = 0
for i in lst:
    if i > max:
        max = i
print("max =", max)
second_max=0
for i in lst:
    if i > second_max and i < max:
        second_max = i
print("second_max", second_max)
