names = ['jane', 'john', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i,j in zip(names, email_domains): #use zip() function for putting two lists together
    print(i,j)

#EXERCISE 1
print("\nEXERCISE 1: ")
def CtoF(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c*9/5+32
        return f

temperatures = [10, -20, -289, 100]

for i in temperatures:
    print(CtoF(i))
