# def = define
def minutes_to_hours(minutes): #passing the parameter: minutes
    hours = minutes / 60
    return hours

def second_to_hours(seconds):
    hours = seconds / 3600
    return hours

print(minutes_to_hours(60), "hour(s)")
print(minutes_to_hours(70), "hours")
print(second_to_hours(7200), "hours")


def say_hello(): #function with no parameter
    return "Hello"

print(say_hello())

#POWER FUNCTION is not ^ its **
#so,
def power(number): #power of 2
   return number**2

print(power(4))