import re

# Function to cipher using Playfair, the text should be cleaned and lowercase
def playfair(text, key):
    # Create the matrix
    matrix = alph_matrix(key)
    # Add x to the text if needed
    text = add_x(text)
    # Create the pairs
    pairs = create_pairs(text)
    # Get the ciphered text
    cipher_text = ""
    for pair in pairs:
        cipher_text += cipher_pair(pair, matrix)
    return cipher_text

#Function to create the alphabet matrix using the key, the key is used to fill the matrix and then the rest of the alphabet is added
def alph_matrix(key):
    # Create the matrix
    alph_matrix = []
    for char in key:
        if char not in alph_matrix:
            alph_matrix.append(char)
    for i in range(26):
        char = chr(i + ord("a"))
        if char not in alph_matrix and char != "j":
            alph_matrix.append(char)
    print(alph_matrix)
    return alph_matrix

def add_x(text):
    # Add x to the text if needed
    new_text = ""
    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if len(pair) == 1:
            pair += "x"
        new_text += pair
    return new_text

def create_pairs(text):
    # Create the pairs
    pairs = []
    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        pairs.append(pair)
    return pairs

def cipher_pair(pair, matrix):
    # Get the positions of the characters in the matrix
    pos1 = matrix.index(pair[0])
    pos2 = matrix.index(pair[1])
    # Get the row and column of each character
    row1 = pos1 // 5
    col1 = pos1 % 5
    row2 = pos2 // 5
    col2 = pos2 % 5
    # Get the ciphered characters
    if row1 == row2:
        cipher1 = matrix[row1 * 5 + (col1 + 1) % 5]
        cipher2 = matrix[row2 * 5 + (col2 + 1) % 5]
    elif col1 == col2:
        cipher1 = matrix[((row1 + 1) % 5) * 5 + col1]
        cipher2 = matrix[((row2 + 1) % 5) * 5 + col2]
    else:
        cipher1 = matrix[row1 * 5 + col2]
        cipher2 = matrix[row2 * 5 + col1]
    return cipher1 + cipher2

##### Clean text ############################

def remove_accents(text):
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for char in text:
        if char in accents:
            text = text.replace(char, accents[char])
    return text

def clean_text(text):
    # Remove the special characters
    text = re.sub(r"[^a-zA-ZñÑ]", "", text)
    # Convert the text to lowercase
    text = text.lower()
    # Remove the accents
    text = remove_accents(text)
    return text

#############################################


if __name__ == "__main__":
    # Read the text from the file
    with open("Texto1.txt", "r", encoding='latin-1') as file: 
        text = file.read()

    text = clean_text(text)
    matrix = alph_matrix("criptografia")