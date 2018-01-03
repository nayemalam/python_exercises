file = open("Files/example.txt", 'r')  # r = read
type(file)
content = file.read()
print(content)

print("\n")

file.seek(0) # point it to the 0th position
new_content = file.readlines()
print(new_content)
content2 = [i.rstrip("\n") for i in new_content] #rstrip is a function to remove a specific element
print(content2)

#ANOTHER FILE
print("\n")
new_file = open("Files/fruits.txt", 'r')
contents = new_file.read()
print(contents)

#CALCULATE LENGTH
print("\n")
new_file = open("Files/fruits.txt", 'r')
contents = new_file.readlines()
for i in contents:
    print(len(i) - 1)
