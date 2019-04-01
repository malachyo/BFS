region1 = "qwertyuiop"
region1 = list(region1)     # creates array of first row keys
region2 = "asdfghjkl"
region2 = list(region2)     # creates array of second row keys
region3 = "zxcvbnm,."
region3 = list(region3)     # creates array of third row keys

msg = input("Input a message.\n").lower()       # takes in user message, converts all characters to lowercase
key = list(input("Input a three-digit key.\n"))     # takes in number of letters to shift each character by (one digit per row)

msg = list(msg)     # creates array of user message

region1key = int(key[0])        # creates integer for each digit in the key
region2key = int(key[1])        # ""
region3key = int(key[2])        # ""

def encrypt():      # function to call for encryption
    newMsg = []     # empty array for newMsg
    for char in msg:
        if char == " ":     # if character is a space, conversion isn't necessary, so immediately added to new message
            newMsg += char
        if char in region1:
            pos = region1.index(char)       # sets position of character to that of its position in the keyboard row
            pos2 = (pos + region1key) % 10      # sets new position to the of its position plus the key shift inputted (loops back if greater than the number 10, number of characters in that row)
            char2 = region1[pos2]       # new character is character in the new position
            newMsg += char2         # add the new character to the new message array
        elif char in region2:       # same but for second row
            pos = region2.index(char)
            pos2 = (pos + region2key) % 9
            char2 = region2[pos2]
            newMsg += char2
        elif char in region3:       # same but for third row
            pos = region3.index(char)
            pos2 = (pos + region3key) % 9      # is % 9 in the second and third region because the last two rows only have 9 characters
            char2 = region3[pos2]
            newMsg += char2
        pos += 1        # adds one to position to move to next character

    output = ""
    output = output.join(newMsg)        # joins all values in the newMsg array into one string named output

    print("Your encrypted message is:\n" + output + ".")        # prints encrypted message with introductory text beforehand, adds a full stop to end of sentence

def decrypt():      # function to call for decryption
    newMsg = []
    for char in msg:
        if char == " ":
            newMsg += char
        elif char in region1:
            pos = region1.index(char)
            pos2 = (pos - region1key) % 10      # function is the same except for calculation of pos2, in which region key is subtracted from the pos in order to decrypt to message's original state.
            char2 = region1[pos2]
            newMsg += char2
        elif char in region2:
            pos = region2.index(char)
            pos2 = (pos - region2key) % 9
            char2 = region2[pos2]
            newMsg += char2
        elif char in region3:
            pos = region3.index(char)
            pos2 = (pos - region3key) % 9
            char2 = region3[pos2]
            newMsg += char2
        pos += 1

    output = ""
    output = output.join(newMsg)

    print("Your decrypted message is:\n" + output + ".")        # outputs decrypted message with introductory text and full stop.


funcInput = input("Would you like to encrypt or decrypt this message? (E/D)\n")     # asks user whether variable msg should be encrypted or decrypted
if funcInput == "E":        # calls function encrypt if user says E
    encrypt()
elif funcInput == "D":      # calls function decrypt if user says D
    decrypt()
else:
    print(funcInput + " is not a valid choice.")        # if user inputs an option that isn't E or D, ends program with error
    exit()
