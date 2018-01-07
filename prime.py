lower = int(input("enter lower number:"))
higher = int(input("enter higher number:"))
for num in range(lower,higher+1):
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
            #    print(num,"is not prime")
               break
        else:
            print(num,"is a prime number") 

    