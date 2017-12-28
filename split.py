input_str=input('enter a string:')
lst=['sachin ramesh tendulkar','rahul kumar dravid','virendra rani sehwag','ms dhoni','irfan pathan']
for name in lst:
    new_lst=name.split(' ')
    if input_str.upper() == new_lst[-1][0].upper():
        print(name)










