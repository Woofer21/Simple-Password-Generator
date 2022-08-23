import random

# Function to generate the random string
def gen(num):
    # Result is the resulting string generated
    # Avail is the available characters which would be made into the new string
    result = ''
    avail = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'

    # Created a for loop which iterates though 0 to what number was inputed, then will generate a random character from the string of aviable to add to the result
    i = 0
    while i < int(num):
        a = avail[random.randrange(0, len(avail))]
        result += a
        i+=1
    
    # Prints the result
    print(result)

# Gets the length of the password from the user
# Then makes a call to the above function with the length inputed
inp = input('Length of password: ')
gen(inp)