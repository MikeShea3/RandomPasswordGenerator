# File: PasswordGenerator.py
# Author: Mike Shea
# Description: A program to generate a password of a user-defined length

import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
            'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

generatedPassword = ""

# User Input
passwordLength = int(input("Enter the number of characters for the password: "))
useNumbers = input("Generate password with numbers? Y/N: ").lower()

while useNumbers.lower() != 'y' and useNumbers.lower() != 'n':
    useNumbers = input("Generate password with numbers? Y/N: ").lower()

if useNumbers == 'y':
    useNumbers = True
else:
    useNumbers = False

# Generate Password
for i in range(passwordLength):

    if useNumbers == False:

        randomInteger = random.randint(0,1)

        # Upper Case Char
        if randomInteger == 0:
            newChar = random.choice(alphabet)
        elif randomInteger == 1:
            newChar = random.choice(alphabet).lower()

        generatedPassword += newChar

    else:
        randomInteger = random.randint(0, 1)

        #Generate Number
        if randomInteger == 0:
            newChar = random.choice(numbers)

        # Generate Char
        elif randomInteger == 1:
            newChar = random.choice(alphabet)

        generatedPassword += newChar
        
# Output
print("Generated password = " + generatedPassword)
