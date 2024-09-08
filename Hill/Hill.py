import re

# Given two letters with their encription, this program will find the key matrix
def keys(a, c, res, b, d, res2):
    list = [(x,y) for x in range(26) for y in range(26) if (a*x + c*y) % 26 == res] #Contains the possible values of a and c
    list2 = [(x,y) for x in range(26) for y in range(26) if (b*x + d*y) % 26 == res2] #Contains the possible values of b and d
    keys = []
    for a, c in list:
        for b, d in list2:
            keys.append((a, b, c, d))
    print(keys)
    return keys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
def Hill_decrypt(text):
    k = keys(18, 7, 4, 18, 11, 18)
    for key in k:
        new = []
        for letter in text:
            new.append(chr((key[0] * (ord(letter) - ord('a')) + key[1] * (ord(letter) - ord('a'))) % 26 + ord('a')))
        if new[len(new)-1] == 's':
            print("".join(new))
            print("\n\n")

#keys(18, 7, 4, 18, 11, 18)

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
    #print(text)
    
    # Remove the accents
    text = remove_accents(text)
    return text

#############################################

if __name__ == "__main__":
    with open("Criptograma_5.txt", "r") as file:
        text = file.read()
    text = clean_text(text)
    Hill_decrypt(text)

