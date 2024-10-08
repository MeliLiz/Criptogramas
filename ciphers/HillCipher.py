import re

#Function to cipher using Hill
def encrypt_hill(text, key, n): # The text should be cleaned and lowercase, the key should be a list of integers and the key matrix is nxn
    #Create the key matrix
    key_matrix = []
    for i in range(n):
        key_matrix.append(key[i * n:(i + 1) * n])
    
    #Add x to the text if needed
    while len(text) % n != 0:
        text += 'x'
    
    #Create the text lists, there will be lists of n characters (their position in the alphabet)
    text_lists = []
    for i in range(0, len(text), n):
        substr = text[i:i + n] # Get the substring of n characters
        list = []
        for char in substr:
            if char != "ñ":
                position = ord(char) - ord("a") # Get the position of the character in the alphabet
            else:
                position = 26

            list.append(position)

        text_lists.append(list)
    #print("Matrix: \n",text_lists, "\n")
    
    # Mulriply the key matrix by the text matrix
    ciphered_lists = [] 
    for list in text_lists: # For each list of n characters
        cipher_list = []
        for i in range(n): # For each row of the key matrix
            sum = 0
            for j in range(n): # For each num of character of the substring
                sum += list[j] * key_matrix[j][i]
            cipher_list.append(sum % 27)
            #print(cipher_list)
        ciphered_lists.append(cipher_list)
    
    #Get the ciphered text
    cipher_text = ""
    for row in ciphered_lists:
        for num in row:
            if num == 26:
                cipher_text += "ñ"
            else:
                cipher_text += chr(num + ord("a"))
    
    return cipher_text

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
    print(text)
    
    # Remove the accents
    text = remove_accents(text)
    return text

#############################################

if __name__ == "__main__":
     # Read the text from the file
    with open("Texto1.txt", "r", encoding='utf') as file: 
        text = file.read()

    text = clean_text(text)

    print("Original\n", text, "\n")
    print("Hill\n", encrypt_hill(text, [3, 4, 2, 5], 2), "\n") # The matrix is invertible mod 27 because gcd(det(matrix), 27) = 1
