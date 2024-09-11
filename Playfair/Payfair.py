# Decipher Playfair using frequencies

import re
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

# Function to get all the bigrams in a text
def get_bigrams(text):
    bigrams = []
    for i in range(0, len(text), 2):
        bigrams.append(text[i:i+2])
    return bigrams

# Function to get the frequency of the bigrams
def get_frequency(bigrams):
    frequency = {}
    for bigram in bigrams:
        if bigram in frequency:
            frequency[bigram] += 1
        else:
            frequency[bigram] = 1
    return frequency

# Function to assign the most common bigrams in spanish to the most common bigrams in the text
def assign_bigrams(frequency):
    letters = "abcdefghijklmnopqrstuvxyz"
    spanish_bigrams = [BLUE+"en"+END, "er", "on", BLUE+"es"+END, "re", "nt", "de", "ar", BLUE +"ci"+END, "ra", "os", "co", "io", "te", "an",
                       "ad", BLUE+"as"+END, "ta", "do", "or", "se", "st", BLUE+"to"+END, "ac", "ue", "in", "ec", "ri", "el", "la", "ro", "no", "ia", "ic", "me", "al", "si", "ne", "na", "ie",
                       BLUE+"qu"+END, "nd", "ti", "le", "tr", "un", "pr", "om", "nc", "da", "ma", "sa", "po", "mi", "pa", "ad", "di", "id", BLUE +"ca"+END, "op", "li", "ni", "oc", "is", "em", "sp", "ed", "od",
                       "ap", "it", "ep", "su", "so", "ol", "eg", "ns", "ea", BLUE+"tu"+END, "pu", "sc", "at", "cu", "ee", "ob", "ce", "et", "lo", 'oa']
    big = [a+b for a in letters for b in letters]
    missing = [bigram for bigram in big if bigram not in spanish_bigrams]
    #print("Missing: ",  missing, "\n")

    #Order the bigrams by frequency
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    assigned = {}
    assigned2 = {} # To store the bigrams that are in the missing list
    for bigram in frequency:
        if spanish_bigrams:
            assigned[bigram] = spanish_bigrams.pop(0)
        else:
            assigned2[bigram] = missing.pop(0)
    return assigned, assigned2

# Function to substitute the bigrams in the text
def substitute_text(text, assigned):
    new_text = []
    for bigram in get_bigrams(text):
        if bigram in assigned:
            new_text.append(assigned[bigram])
        else:
            new_text.append(bigram)
    return new_text

# Function to substitute all the ocurrences of a bigram in the text list
def substitute_bigram(text, bigram, new_bigram):
    new_text = []
    for i in range(0, len(text)):
        if text[i] == bigram:
            new_text.append(new_bigram)
        else:
            new_text.append(text[i])
    return new_text

def decrypt_playfair(text, key): # The key is a string with the 25 letters of the key
    # Create the matrix
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key[i*5 + j])
        matrix.append(row)
    print(matrix)

    # Get the bigrams
    bigrams = get_bigrams(text)
    #print(bigrams)

    # Decrypt the text
    new_text = []
    for bigram in bigrams:
        row1, col1 = divmod(key.index(bigram[0]), 5)
        row2, col2 = divmod(key.index(bigram[1]), 5)
        if row1 == row2:
            new_text.append(matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            new_text.append(matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2])
        else:
            new_text.append(matrix[row1][col2] + matrix[row2][col1])
    print(new_text)
    return "".join(new_text)

def color_elems(bigrams,list, color):
    new_list = []
    for bigram in bigrams:
        if bigram in list:
            new_list.append(color + bigram + END)
        else:
            new_list.append(bigram)

    return "".join(new_list)



if __name__ == "__main__":
    with open("Criptograma6.txt", "r") as file:
        criptograma = file.read()

    BLUE = '\033[94m'
    END = '\033[0m'
    text = clean_text(criptograma)
    bigrams = get_bigrams(text)
    #frequency = get_frequency(bigrams)
    #print(frequency, "\n")
    #assigned, assigned2 = assign_bigrams(frequency)
    #subst = substitute_text(text, assigned)
    #print(bigrams)
    """
    subst1 = substitute_bigram(bigrams, "nm", BLUE +"ca"+ END)
    subst3 = substitute_bigram(subst1, "jo", BLUE +"pi"+ END)
    subst4 = substitute_bigram(subst3, "ux", BLUE +"tu"+ END)
    subst5 = substitute_bigram(subst4, "nl", BLUE +"lo"+ END)
    subst6 = substitute_bigram(subst5, "gn", BLUE +"el"+ END)
    subst7 = substitute_bigram(subst6, "cy", BLUE +"ox"+ END)
    subst8 = substitute_bigram(subst7, "sl", BLUE +"tr"+ END)
    subst9 = substitute_bigram(subst8, "fb", BLUE +"es"+ END)
    print("".join(subst9))"""

    #key = "bdrzfiolncjpgehkytuxvqsam"
    #key = "fhramiolncjpgetbdkquvyzsx"
    key = "fhramiolncjpgetbdkquvyzsx"
    decrypted = decrypt_playfair(text, key)
    decr_bigr = get_bigrams(decrypted)
    decrypted = color_elems(decr_bigr,['ca', 'pi', 'tu', 'lo', 'ox', 'el'], BLUE)


    print("".join(decrypted))