alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

def encrypt():
    outputMsg = ""      # space for encrypted message
    inputMsg = input("Input message to encrypt.\n")     # input for message to be encrypted
    for character in inputMsg:
        for num in numbers:
            if character == num:    # checks input message only contains letters
                print("Message must only contain letters.")
                exit()

    shiftBy = input("Input number of letters to shift by.\n")   # input for shift down the alphabet each letter will be
    for character in shiftBy:
        if character.isalpha():
                print("Must be integer value to encrypt.")  # checks shift value doesn't contains letters
                exit()

    shiftBy = int(shiftBy)  # converts shift value to integer


    for letter in inputMsg:
        pos = alphabet.index(letter)    # sets position of each letter in inputted message to its index value
        pos2 = (pos + shiftBy) % 26     # sets new position to original position added to shift value, ensures loops back after 26 letters in alphabet
        letter2 = alphabet[pos2]        # creates new letter set to the new position after shift
        outputMsg += letter2            # encrypted message is all shifted letters combined.

    print("Your encrypted message is", outputMsg)   # outputs encrypted message

def decrypt():
    outputMsg = ""
    inputMsg = input("Input message to decrypt.\n")
    for character in inputMsg:
        for num in numbers:
            if character == num:
                print("Message must only contain letters.")
                exit()

    shiftBy = input("Input given key shift value.\n")
    for character in shiftBy:
        if character.isalpha():
                print("Must be integer value to encrypt.")
                exit()

    shiftBy = int(shiftBy)


    for letter in inputMsg:
        pos = alphabet.index(letter)
        pos2 = (pos - shiftBy) % 26     # subtracts shift from position this time to return encrypted letters back to original
        letter2 = alphabet[pos2]
        outputMsg += letter2

    print("Your decrypted message is", outputMsg)      # outputs decrypted message



userChoice = input("Would you like to encrypt or decrypt a message?\n")
# taking in users decision of whether to encrypt or decrypt
if userChoice == "encrypt":
    encrypt()   # execute encrypt function
elif userChoice == "decrypt":
    decrypt()   # execute decrypt function
else:
    print("Must choose either 'encrypt' or 'decrypt'")  # in case input is neither, end program
    exit()
