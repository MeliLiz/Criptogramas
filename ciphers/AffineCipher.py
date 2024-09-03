import re

# Affine cipher
def encrypt_affine(text, a, b): # The text should be cleaned and lowercase
    cipher_text = ""
    for char in text:
        start = ord("a") #get the ASCII value of 'a'
        pos = ord(char) - start # get the position of the text char in the alphabet
        new_pos = (a * pos + b) % 26 # get the new position of the char in the alphabet
        cipher_text += chr(start + new_pos)
    return cipher_text

#Affine cipher using a 27 character alphabet using yhe ñ character
def encrypt_affine_27(text, a, b): # The text should be cleaned and lowercase
    cipher_text = ""
    for char in text:
        start = ord("a")
        pos = ord(char) - start
        new_pos = (a * pos + b) % 27 # get the new position of the char in the alphabet considering the ñ character
        if new_pos == 26: # if the new position is 26, the character is ñ
            cipher_text += "ñ"
        else:
            cipher_text += chr(start + new_pos)
    return cipher_text

########### Clean text ########################

def remove_accents(text):
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for char in text:
        if char in accents:
            text = text.replace(char, accents[char])
    return text

def clean_text(text):
    # Remove the special characters
    text = re.sub(r"[^a-zA-Z]", "", text)
    # Convert the text to lowercase
    text = text.lower()
    # Remove the accents
    text = remove_accents(text)
    return text

###############################################

if __name__ == "__main__":
     # Read the text from the file
    with open("Texto1.txt", "r", encoding='latin-1') as file: 
        text = file.read()

    text = clean_text(text)
    print("Original\n", text, "\n")
    # print("Affine\n", encrypt_affine(text, 5, 7), "\n")
    print("Affine 27\n", encrypt_affine_27(text, 5, 7), "\n")
