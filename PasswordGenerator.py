# Filename: PasswordGenerator.py
# Author: Mike Shea
# Description: PasswordGenerator.py generates a password from
# upper and lower case chars with optional numbers and alternate characters.

# Does not generate alt chars yet

import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
            'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

altChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '`', '~', '{', '{', ']', '}', ';', ':',
            ',', '<', '>', '.', '?', '/']

generatedPassword = ""

# USER INPUT
# Length
passwordLength = int(input("Enter the number of characters for the password: "))

# Numbers
useNumbers = input("Generate password with numbers? Y/N: ").lower()

while useNumbers.lower() != 'y' and useNumbers.lower() != 'n':
    useNumbers = input("Generate password with numbers? Y/N: ").lower()

if useNumbers == 'y':
    useNumbers = True
else:
    useNumbers = False

# Alternate Characters
useAltChars = input("Generate password with alternate characters? Y/N: ").lower()

while useAltChars.lower() != 'y' and useAltChars.lower() != 'n':
    useAltChars = input("Generate password with alternate characters? Y/N: ").lower()

if useAltChars == 'y':
    useAltChars = True
else:
    useAltChars = False

# GENERATE PASSWORD
for i in range(passwordLength):

    if useNumbers == False:

        randomInteger = random.randint(0,1)

        # Upper Case
        if randomInteger == 0:
            newChar = random.choice(alphabet)
        # Lower Case
        elif randomInteger == 1:
            newChar = random.choice(alphabet).lower()

        generatedPassword += newChar

    else:
        randomInteger = random.randint(0, 2)

        #Generate Number
        if randomInteger == 0:
            newChar = random.choice(numbers)

        # Generate Lower Case
        elif randomInteger == 1:
            newChar = random.choice(alphabet).lower()
            
        # Generate Upper Case
        elif randomInteger == 2:
            newChar = random.choice(alphabet)

        generatedPassword += newChar
        
# Output
print("Generated password = " + generatedPassword)
input()
