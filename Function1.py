#create a divide function
def divide(a,b):
    try:
        return a/b
    except:
        return "You are dividing by zero"

print(divide(1,0))

def multiply(a,b):
    return a*b

print(multiply(3,5))