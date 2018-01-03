str1 = "this is a book this is a good book"
sub = "is"
n = len(str1)
i = 0
flag = 0
while i < n:
    pos = str1.find(sub,i,n)
    if pos == -1:
        break
    else:
        print("found at position ",pos+1)
        i = pos+1
        flag = flag + 1
if flag == 0:
    print("not found.")
else:
    print("no. of sub string is ",flag)
    
