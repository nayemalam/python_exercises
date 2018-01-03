from datetime import datetime

#name = input("What is your name? ") #get users input
#age = int(input("How old are you? "))
curYear = datetime.now().year;
curMonth = datetime.now().month;
# curMonth = int(input("Enter your month: ")) #convert input to an integer!

if curMonth == 12: #if statements end with : not {
    print("December")
elif curMonth == 11: #else if statements are called elif
    print("November")
elif curMonth == 10:
    print("October")
elif curMonth == 9:
    print("September")
elif curMonth == 8:
    print("August")
elif curMonth == 7:
    print("July")
elif curMonth == 6:
    print("June")
elif curMonth == 5:
    print("May")
elif curMonth == 4:
    print("April")
elif curMonth == 3:
    print("March")
elif curMonth == 2:
    print("February")
elif curMonth == 1:
    print("January")
# print(curMonth)
# print(curYear)

#result = 100 - age
#year = curYear + result
#print("In",year,"you will be 100 years old")

c = "Hi There!" # any variable can be declared without stating its type
for i in range(len(c)): #end a for loop with : not {
    print(c[i], end = "") #you use the ' end = "" ' to print it on one line! Python3

