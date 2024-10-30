#Izail Chamberlain
# UWYO COSC 1010
# Submission Date:10/29/24
# HW 02
# Lab Section: 11
# Sources, people worked with, help given to: ChatGPT for clarification, definitions, and rephrasing of concepts
# your
# comments
# here

#Assignment Template

#Homework 2
#Due Tuesday by 11:59pm Points 50 Submitting a file upload File Types py Available until Nov 1 at 11:59pm
#For this homework assignment you will be writing a program that translates between plaintext and Morse Code.

#When your program first starts it should ask the user for the input string. If plaintext alphabet cahracters is entered output the Morse Code equivalent.

#You may assume that only alphabet characters will be entered, and may ignore other input characters.

#You can use the equivalencies below.

#A: .-          N: -.
#B: -...        O: ---
#C: -.-.        P: .--.
#D: -..         Q: --.-
#E: .           R: .-.
#F: ..-.        S: ...
#G: --.         T: -
#H: ....        U: ..-
#I: ..          V: ...-
#J: .---        W: .--
#K: -.-         X: -..-
#L: .-..        Y: -.-- 
#M: --          Z: --..

#Your program should output the correct Morse Code regardless of casing of the input characters. You should output spaces in the input string as two spaces, and separation between  Morse Code characters should be a single space.

#For example the message 'Go Pokes' would be equivalent to:
#--. ---  .--. --- -.- . ...

#Where there is a space between the "G" and "o" in Morse code and two spaces between the "Go" and "Pokes".

#Tips and tricks:

#Dictionaries will be your friend for this assignment
#You can utilize the `isalpha()` method on a string to see if it is  an alphabet character
#`if string_variable.isalpha():`
#The Morse Code characters will only ever be `-` or `.`  or a space
#You can treat strings much like you would a list, meaning you can iterate through them and access characters based on an index position
#Remember you can utilize string concatenation with `+=` to build new strings
#Name your file: LastnameFirstname-HW02.py

#Your file MUST include the standard comments at the top of the file that are expected with the labs.
# Your Name Here
# UWYO COSC 1010
# Submission Date
# HW 02
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here

# Morse code dictionary
morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',  
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---', 
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',  
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--', 
    'Z': '--..'
}

def translate_to_morse(plaintext): #defining function 
    morse_output = ""
    for char in plaintext:
        if char.isalpha():  # Checks if the character is an alphabet letter
            morse_output += morse_code_dict[char.upper()] + " "
        elif char == " ":  # Adds two spaces for word separation
            morse_output += "  "
    return morse_output.strip()  # Removes trailing space behind character

input_text = input("Enter text to translate to Morse Code: ") #Prompts input from the user
morse_translation = translate_to_morse(input_text) #executes translation from user unput
print("Morse Code:", morse_translation) #returns the corresponding morse code from the given input
