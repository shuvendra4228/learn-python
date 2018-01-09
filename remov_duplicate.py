def remov_duplicat(n):
    list_without_duplicat = []
    for items in list_duplicat:
        if items not in list_without_duplicat:
            list_without_duplicat.append(items)
    return list_without_duplicat

list_duplicat = [int(item) for item in input('enter your element:').split(" ")]
x = remov_duplicat(list_duplicat)
print(x)

