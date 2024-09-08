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
    print("Missing: ",  missing, "\n")

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



if __name__ == "__main__":
    with open("Criptograma6.txt", "r") as file:
        criptograma = file.read()

    BLUE = '\033[94m'
    END = '\033[0m'
    text = clean_text(criptograma)
    bigrams = get_bigrams(text)
    frequency = get_frequency(bigrams)
    #print(frequency, "\n")
    assigned, assigned2 = assign_bigrams(frequency)
    subst = substitute_text(text, assigned)
    subst1 = substitute_bigram(subst, "jo", BLUE +"pi"+ END)
    subst3 = substitute_bigram(subst1, "os", BLUE +"lo"+ END)
    subst4 = substitute_bigram(subst3, "sl", BLUE +"tr"+ END)
    subst5 = substitute_bigram(subst4, "er", BLUE +"es"+ END)
    #print(subst5)
    #print("".join(subst5))
