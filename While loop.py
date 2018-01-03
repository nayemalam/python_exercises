passwd = " "
while passwd != "hello":
    passwd = input("\nEnter the password: ")
    if passwd == "hello!":
        print("YOU GOOD")
        break
    else:
         print("you are wrong!")
