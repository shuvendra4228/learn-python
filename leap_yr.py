# user will input the year
# Leap Year | Not Leap Year

year = int(input("enter a year:"))

if year % 100 == 0 and year % 400 == 0 :
          print("Leap")
elif year % 4 == 0:
    print("Leap")
else :
    print("Not leap")