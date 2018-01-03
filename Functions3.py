#Advanced Functions

def minutes_to_hours(minutes, seconds):
    hours = (minutes / 60) + (seconds / 3600)
    return hours

print(minutes_to_hours(70, 300))
print(type(minutes_to_hours(70, 300)))

#POWER FUNCTION
def power(base, exponent):
    return base**exponent

print(power(2,3))