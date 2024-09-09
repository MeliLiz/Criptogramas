import re

# Get all the possible matrix keys invertible mod 26
def get_invertible_keys():
    keys = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    if gcd(i*l - j*k, 26) == 1:
                        keys.append([i, j, k, l])
    return keys

# Get the gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Get the digrams of a text
def get_digram(text):
    digrams = []
    for i in range(0, len(text), 2):
        digrams.append(text[i:i+2])
    return digrams

def get_number_digrams(text):
    digrams = get_digram(text)
    number_digrams = []
    for digram in digrams:
        number_digrams.append([ord(digram[0])-97, ord(digram[1])-97])
    return number_digrams

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
    text = re.sub(r"[^a-záéíóú]", "", text)
    
    # Remove the accents
    text = remove_accents(text)
    
    # Ensure even number of characters
    if len(text) % 2 != 0:
        text += 'x'  # Add 'x' as padding if needed
    return text

#############################################

# Multiply a key by a digram
def multiply_key_digram(key, digram):
    a = key[0]*digram[0] + key[2]*digram[1]
    b = key[1]*digram[0] + key[3]*digram[1]
    return [a % 26, b % 26]

# Try every key on every digram
def decipher(text):
    keys = get_invertible_keys()  # Get all invertible keys
    digrams = get_number_digrams(text)  # Get digrams from the text

    for key in keys:
        res1 = []
        for digram in digrams:
            res = multiply_key_digram(key, digram)
            res1.append([chr(i + 97) for i in res])  # Convert numbers back to letters
        
        # Join the result into a single string
        res1 = "".join(["".join(i) for i in res1])
        
        # Check if the fifth and last positions match the given letters
        if res1[-1] == "s" and res1[4] == "e" and 'w' not in res1:  # -1 is last, 4 is fifth
            print("Key:", key)
            print("Decrypted text:", res1)
            print("\n")

if __name__ == "__main__":
    with open("Criptograma_5.txt", "r") as file:
        text = file.read()
    
    text = clean_text(text)  # Clean the text

    decipher(text)  # Attempt to decipher with all keys
