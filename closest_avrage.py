import sys

numbers = [int(item) for item in input("Enter the numbers ").split(" ")]

closest_avg = None # This will store the result
avrage = 0 # This will store the avrage of the sum of all elements of the list
diff = sys.maxsize # A highly postetive int

# Find the avrage of sum
for number in numbers:
    avrage += number
avrage = avrage / len(numbers)

# Scan to find the closest number to avrage
for number in numbers:
    if abs(avrage - number) < diff:
        closest_avg = number
        diff = abs(avrage - number)


print(closest_avg)