import re

# Function to cipher using Playfair, the text should be cleaned and lowercase
def playfair(text, key):
    # Create the matrix
    letters = alph_matrix(key)
    pairs_ = pairs(text)

    # Get the ciphered text
    cipher_text = ""
    for pair in pairs_:
        cipher_text += cipher(pair, letters)
    return cipher_text

#Function to create the alphabet matrix using the key, the key is used to fill the matrix and then 
# the rest of the alphabet is added
def alph_matrix(key):
    # Create the matrix 5x5, represented as a list
    alph_matrix = []
    for char in key:
        if char not in alph_matrix:
            alph_matrix.append(char)
    # This alphabet will not include ñ because it can be represented by n
    # Iterate over the ascii values of the alphabet (26 letters, ñ not included)
    # Not considering the letter w because it is the less used letter so it will be represented as v
    for i in range(26): 
        char = chr(i + ord("a"))
        if char not in alph_matrix and char != "w":
            alph_matrix.append(char)
    #print(alph_matrix)
    return alph_matrix

# Function to get pairs of chars from the text
#If the pair has two chars of the same value, an x is added
def pairs(text):
    pairs = []
    i=0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                pairs.append(text[i] + "x")
                i += 1
            else:
                pairs.append(text[i] + text[i + 1])
                i += 2
        else:
            pairs.append(text[i] + "x")
            i += 1
    return pairs

def cipher(pair, list): # The list is the matrix
    # Get the positions of the characters in the matrix
    elem1 = pair[0]
    elem2 = pair[1]

    if elem1 == "ñ":
        elem1 = "n"
    elif elem1 == "w":
        elem1 = "v"
    if elem2 == "ñ":
        elem2 = "n"
    elif elem2 == "w":
        elem2 = "v"

    pos1 = list.index(elem1)
    pos2 = list.index(elem2)

    row1 = pos1 // 5 # Get the num row
    col1 = pos1 % 5 #Get the num col
    row2 = pos2 // 5
    col2 = pos2 % 5

    #As we are working with a list
    #row * 5 gets us to the position of the row
    #sum the row so that we are in the position of the char
    #% 5 to get the column, because the matrix should be ciclic
    if row1 == row2: # If the characters are in the same row, the character to the right is taken
        cipher1 = list[row1 * 5 + (col1 + 1) % 5]
        cipher2 = list[row2 * 5 + (col2 + 1) % 5]
    elif col1 == col2: # If the characters are in the same column, the character below is taken
        cipher1 = list[((row1 + 1) % 5) * 5 + col1]
        cipher2 = list[((row2 + 1) % 5) * 5 + col2]
    else: # If the characters are in different rows and columns, the characters are exchanged
        cipher1 = list[row1 * 5 + col2]
        cipher2 = list[row2 * 5 + col1]
    return cipher1 + cipher2

##### Clean text ############################

def remove_accents(text):
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for char in text:
        if char in accents:
            text = text.replace(char, accents[char])
    return text

def clean_text(text):
    # Convert the text to lowercase
    text = text.lower()
    # Remove the special characters
    text = re.sub(r"[^a-zñáéíóú]", "", text)
    #print(text)
    
    # Remove the accents
    text = remove_accents(text)
    return text

#############################################


if __name__ == "__main__":
    # Read the text from the file
    with open("Texto1.txt", "r", encoding='utf') as file: 
        text = file.read()

    text = clean_text(text)
    #matrix = alph_matrix("criptografia")
    print("Original\n", text, "\n")
    #print(pairs(text))
    #print(pairs("hello"))
    print("Encrypted\n", playfair(text, "cripto"), "\n")