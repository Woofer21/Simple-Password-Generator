import random

def gen(num):
    result = ''
    avail = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'

    i = 0
    while i < int(num):
        a = avail[random.randrange(0, len(avail))]
        result += a
        i+=1
    
    print(result)

inp = input('Length of password: ')
gen(inp)