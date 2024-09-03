import re

# Vigenere cipher
def encrypt_vigenere(text, key):
    key = key.lower()
    length_key = len(key)
    length_text = len(text)
    key = key * (length_text // length_key) + key[:length_text % length_key] # The key is repeated to the length of the text
    cipher_text = ""
    for i in range(length_text):
        if text[i].isalpha():
            if text[i].islower():
                cipher_text += chr((ord(text[i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a')) 
            else:
                cipher_text += chr((ord(text[i]) - ord('A') + ord(key[i]) - ord('a')) % 26 + ord('A'))
        else:
            cipher_text += text[i]
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

def count_characters(text):
    # Count the frequency of each character
    dict_ = {}
    for char in text:
        if char in dict_:
            dict_[char] += 1
        else:
            dict_[char] = 1
    return dict_

if __name__ == "__main__":
    # Read the text from the file
    with open("AlquimistaReduced.txt", "r", encoding='latin-1') as file: # AlquimistaReduced.txt has 1670 characters cleaned
        text = file.read()

    text = clean_text(text)
    print(text)
    #print(encrypt_vigenere(text, "criptografia"))