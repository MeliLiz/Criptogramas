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

def keys_1(a, b, res, c, d, res2):
    list = [(x,y) for x in range(26) for y in range(26) if (a*x + b*y) % 26 == res] #Contains the possible values of a and c
    list2 = [(x,y) for x in range(26) for y in range(26) if (c*x + d*y) % 26 == res2] #Contains the possible values of b and d
    keys = []
    for a, b in list:
        for c, d in list2:
            keys.append((a, b, c, d))
    return keys

def keys_2():
    keys = []
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    keys.append((a, b, c, d))
    return keys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_bigrams(text):
    bigrams = []
    for i in range(len(text)-1):
        bigrams.append(text[i:i+2])
    return bigrams

def get_numbers(bigrams):
    numbers = []
    for bigram in bigrams:
        numbers.append([ord(bigram[0])-97, ord(bigram[1])-97])
    return numbers

# Test cases
def Hill_decrypt(text):
    numbers = get_numbers(get_bigrams(text))
    k = keys_2()
    for key in k:
        new = []
        for bigram in numbers:
            a, b = bigram
            x = (key[0]*a + key[1]*b) % 26
            y = (key[2]*a + key[3]*b) % 26
            new.append([x+97, y+97])
        if new[2][0] == 4 and new[len(new)-1][1] == 18:
            print(key)
            print(new)
            break
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

