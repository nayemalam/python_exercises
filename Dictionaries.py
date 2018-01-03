# Another data type: dictionary
list = ["soemthing", 3, " random"] # this is a list
dictionary = {"Name":"Nayem", "Surname":"Alam"} # this is a dictionary
# for the code above, the Name is a key, Nayem is the value. Similarly, Surname is key, and Alam is value

print(dictionary["Name"])
print(dictionary)

d = {"Name":"Nayem", "Surname":"Alam", "Cities": ("Montreal, Quebec, Porto", "nybz", 'shuor')}
#the one in the brackets is a tuple
#so
print(d["Cities"]) #prints a tuple
#so if we do:
#print(d["Cities"][4]) #prints out the 4th index if it was ("Montreal, Quebec, Porto") one word
print(d["Cities"][2]) #prints out the 2nd item