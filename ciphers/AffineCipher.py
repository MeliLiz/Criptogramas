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

if __name__ == "__main__":
     # Read the text from the file
    with open("Texto1.txt", "r", encoding='latin-1') as file: 
        text = file.read()

    text = clean_text(text)
    print("Original\n", text, "\n")
