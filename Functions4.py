#FUNCTIONS AND USER INPUTS
age = input("Enter you age fam ")
new_age = float(age) + 50 #global variable
print(new_age)

def age_foo(age):
    new_age = float(age) + 50 #local variable
    return new_age

print(age_foo(12))
