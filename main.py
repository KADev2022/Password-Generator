import random

# This will prompt the user to enter the size of the password
n = int(input("Enter the size of the password you need: "))


# The passwordGenerator() method will generate a password
def passwordGenerator(n):
    # Defined strings
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    special = '!@#$%&*'

    # The password is assigned to n number of characters
    password = ''

    for i in range(n):
        l = [random.choice(lower), random.choice(upper), random.choice(number), random.choice(special)]
        password = password + random.choice(l)

    return password


print('Your randomly generated password is:', passwordGenerator(n))
