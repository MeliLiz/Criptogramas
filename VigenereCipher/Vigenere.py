import re

# Vigenere cipher
def encrypt_vigenere(text, key): # The text should be cleaned and lowercase
    key = key.lower()
    length_key = len(key)
    length_text = len(text)
    key = key * (length_text // length_key) + key[:length_text % length_key] # The key is repeated to the length of the text
    cipher_text = ""
    for i in range(length_text):
        char_text = text[i]
        char_key = key[i]
        start = ord("a") #get the ASCII value of 'a'
        pos_alph= ord(char_text) - start # get the position of the text char in the alphabet
        pos_key = ord(char_key) - start # get the position of the key char in the alphabet
        new_pos = (pos_alph + pos_key) % 26 # get the new position of the char in the alphabet
        cipher_text += chr(start + new_pos) # get the new char
    return cipher_text


############## Clean text ############################

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

######################################################

def count_characters(text):
    # Count the frequency of each character
    dict_ = {}
    for char in text:
        if char in dict_:
            dict_[char] += 1
        else:
            dict_[char] = 1
    return dict_


def coincidence_index(text):
    # Clean the text
    text = clean_text(text)
    # Count the number of characters
    n = len(text)
    # Count the frequency of each character
    dict_ = count_characters(text)
    # Calculate the coincidence index
    count = 0
    for char in dict_:
        count += dict_[char] * (dict_[char] - 1)
    count /= n * (n - 1)
    return count


if __name__ == "__main__":
    # Read the text from the file
    with open("AlquimistaReduced.txt", "r", encoding='latin-1') as file: # AlquimistaReduced.txt has 1670 characters cleaned
        text = file.read()

    text = clean_text(text)
    inp = input("Enter the key: ")
    print("Original\n", text, "\n")
    # print("Encrypted\n", encrypt_vigenere(text, "criptografia"), "\n")
    encrypted = encrypt_vigenere(text, inp)
    print("Encrypted\n", encrypted, "\n")
    print("Coincidence index: ", coincidence_index(encrypted))
