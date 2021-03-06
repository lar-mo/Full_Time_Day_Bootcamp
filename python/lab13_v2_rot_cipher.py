# filename: lab13_v2_rot_cipher.py
'''
Lab 13: ROT Cipher

Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language,
so encryption is the same as decryption.

Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
'''

# import the string libraries
import string

# Set variables
# Create base_alphabet from string library
base_alphabet = string.ascii_lowercase
# prompt the user for a string
user_string = input("Enter a lowercase word to ROT encrypt: ")
while True:
    amount_of_rotation = int(input("Enter the rotation amount (1 or higher): "))
    if amount_of_rotation < 1: # or amount_of_rotation > 26:
        print("Invalid amount. Try again!")
    break

### Solution 1 ###
### (1) generate full, 26-character rotated alphabet
### (2) find ids of input letters, return output letters with same ids from rotated alphabet
# Generate rotN_alphabet based on base_alphabet
rotN_alphabet_list = []
for letter in base_alphabet:
    rotN_alphabet_list.append(base_alphabet[(base_alphabet.find(letter) + amount_of_rotation) % 26]) # uses index for base_alphabet list
    rotN_alphabet = ''.join(rotN_alphabet_list)

# for each character, find the corresponding character
rotN_letters = []
for letter in user_string:
    id_for_letter = base_alphabet.find(letter)                              # part of solution 1
    ### Solution 2 ###
    ### (1) find ids of input letters
    ### (2) rotate the input letters
    ###     add the input amount to the id and use modulus
    ###     to confine the rotation to len(base_alphabet)
    # orig_id_for_letter = base_alphabet.find(letter)                       # part of solution 2; find ids
    # rot_id_for_letter = (orig_id_for_letter + amount_of_rotation) % 26    # part of solution 2; do math on ids

    # add corresponding character to an output string
    rotN_letters.append(rotN_alphabet[id_for_letter])                       # part of solution 1
    # rotN_letters.append(base_alphabet[rot_id_for_letter])                 # part of solution 2

    # convert list to string
    rotN_string = ''.join(rotN_letters)

# print
print(f"ROT{amount_of_rotation}: '{rotN_string}'")
