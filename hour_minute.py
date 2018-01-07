def hour_min(hr,min):
    total_mins = hr*60 + min
    return 0.5*total_mins
hour = int(input("enter hour: "))
minute = int(input("enter minute: "))
watch = hour_min(hour,minute)
print(f'hour hand moves {watch} degrees in {hour} hr and {minute} minutes')








