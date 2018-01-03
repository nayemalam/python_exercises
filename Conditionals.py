##BASIC
# a = int(input("Enter a number "))
a = 5

if a < 5:
    print(a, "is Less than 5")
elif a == 5:
    print(a, "is Equal to 5")
else:
    print(a, "is Greater than 5")


# ADVANCED
def age_foo(age):
    new_age = float(age) + 50
    return new_age


age = float(input("Enter your age: "))

if age < 150:
    print(age_foo(age))
else:
    print("How is that possible?")

# EXERCISE 1
print("\nEXERCISE 1: ")


def s_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers do not have a length"
    else:
        return len(mystring)

print(s_length(12))

# EXERCISE 2
print("\nEXERCISE 2: ")

def new_s_length(mystring): #NOTE: you could've written s_length too as the name: this is called: OVERLOADING
    if type(mystring) == int:
        return "Sorry, integers do not have a length"
    elif type(mystring) == float:
        return "Sorry, floats do not have a length"
    else:
        return len(mystring)

print(new_s_length(13.0))

# EXERCISE 3
print("\nEXERCISE 3: ")

def CtoF(c):
    if c < -273.15:
        return "impossible!"
    else:
        f = c * 9 / 5 + 32
        return f

print(CtoF(-273.4))
