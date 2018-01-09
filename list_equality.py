list_integer = [1,2,3,4,5, 6]
list1_integer = [5,4,2,3,6, 1, 1]
if len(list_integer) != len(list1_integer):
    print("Not same")
else :
    for item in list_integer:
        if item not in list1_integer:
            print("Not same")
            break
    else :
        print("Same")
