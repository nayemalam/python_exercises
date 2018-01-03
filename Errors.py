#Syntax Errors
print(1)
#int 3
int(3)
animal = "walrus"
number = 2
print(number)
print(animal)
#print 3 -- error, need brackets around it

#Runtime Errors
a = 1
b = "3"
#print(int(2.5))
print(float(2.5)) #need proper data type
#print(a+b)
print(a+int(b)) # need to cast it