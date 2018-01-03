File = open("/Users/nayemalam/PycharmProjects/pythonExercises/Files/examples.txt", 'w') #creating an example.txt and w = write
numbers = [1,2,3]


#APPEND TO A TEXT FILE
new_file = open("/Users/nayemalam/PycharmProjects/pythonExercises/Files/examples.txt", 'a') #a = append
# Write text on top of wtv is there already
new_file.write("Duizd")
new_file.write("\nAnything1")
new_file.write("\nAnything2")
new_file.write("\nAnything3")
new_file.write("\nAnything4")

#OTHER METHODS TO KNOW:
# r+/w+ : You can both read and write. Difference between r+ and w+ is that w+ you can overwrite
# your existing file, whereas r+ places pointer at the beginning of the file
# a+ : places pointer at the end of the file

# EXERCISE 1:
print("\nEXERCISE 1: ")

temperatures = [10, -20, -289, 100]


def writer(temperatures, filepath):
    with open(filepath, 'w') as file: #saves it in the same folder as project
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n") #same thing as printing/returning the function


writer(temperatures, "temps.txt")  #Here we're calling the function, otherwise no output will be generated