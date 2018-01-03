# Same thing as file = open(??) but now you don't have to write File.close()
with open("/Users/nayemalam/PycharmProjects/pythonExercises/Files/examples.txt", 'a+') as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine7")

