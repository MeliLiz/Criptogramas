
import re

#Function to count the number of letters in a text
def count_letters(text):
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    print(letters, "\n")
    return letters

# Function to sort the letters by the number of times they appear
def sort_letters(text):
    counts = count_letters(text)
    def get_count(letter):
        return counts[letter]
    return sorted(counts.keys(), key=get_count, reverse=True)

# Function to get the sustitutions of the letters in the criptograma in a dictionary
def get_sustitutions(criptograma, freq_ordered_letters):
    letters = sort_letters(criptograma) # Letters in the criptograma ordered by the number of times they appear
    print(letters)
    sustitution = {}
    for i in range(len(letters)):
        sustitution[letters[i]] = freq_ordered_letters[i]
    return sustitution

# Function to sustitute the letters in the text
# Order_freq_letters is a list with the letters ordered by the number of times they tend to appear in a text
def sustitute_text(text, order_freq_letters):
    sustitutions = get_sustitutions(text, order_freq_letters)
    new_text = []
    for letter in text:
        if letter.isalpha():
            new_text.append(sustitutions[letter])
        else:
            new_text.append(letter)
    return "".join(new_text)


def repeated_substrings(text):
    # Clean the text
    text = clean_text(text)
    dict_ = {}
    length = len(text)
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            substring = text[i:j]
            if substring in dict_:
                dict_[substring][0] += 1
                dict_[substring][1].append(i) # Store the position of the substring
            else:
                dict_[substring] = 1
                dict_[substring] = [1, [i]]

    repeated_substrings ={k: v for k, v in dict_.items() if v[0] > 1 and len(k) > 1}
    # Sort the dictionary by the length of the substring
    repeated_substrings = dict(sorted(repeated_substrings.items(), key=lambda item: len(item[0]), reverse=True))
    # Sort the dictionary by the number of times the substring is repeated
    repeated_substrings = dict(sorted(repeated_substrings.items(), key=lambda item: item[1][0], reverse=True))
    return repeated_substrings

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

# Function to find the alpha and beta using an queation system
# First we say that z originally is an l and l is an a
# 
def find_alpha_beta(val, sup1, val2, sup2): 
    diff_val = val - val2
    diff_sup = sup1 - sup2
    inverse = [x for x in range(26) if (x * diff_sup) % 26 == 1]
    
    if len(inverse) == 0:
        print("There is no inverse")
        return None
    
    alpha = diff_val * inverse[0] % 26
    beta = (val2 - (alpha * sup2)) % 26
    
    return alpha, beta


def substitute_text(text, alpha, beta):
    new_text = []
    for letter in text:
        a_val = ord('a')
        letter_val = ord(letter.lower()) - a_val 
        # original * alpha + beta =  encrypted mod 26
        # original = (encrypted - beta) * alpha^-1 mod 26
        inverse = [x for x in range(26) if (x * alpha) % 26 == 1]
        original = chr(((letter_val - beta) * inverse[0] % 26) + a_val)
        new_text.append(original)
            
    return "".join(new_text)

    
    
    

if __name__ == "__main__":

    BLUE = '\033[94m'
    END = '\033[0m'
    
    with open("Criptograma3.txt", "r") as file:
        criptograma = file.read()
    
    text = clean_text(criptograma)
    print("Text:\n", text, "\n")
    #print(sort_letters(text))
    
    freq_ordered_letters_1 = ['e', BLUE+'a'+END, 'o', 's', 'r', 'n', 'i', 'd', BLUE+'l'+END, 'c', 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k']
    print(sustitute_text(text.lower(), freq_ordered_letters_1))

    
    """repeated = repeated_substrings(text)
    for key in repeated:
        print(key, repeated[key][0])"""
    
    """for i in range(1, 26):
        for j in range(1, 26):
            try:
                alpha, beta = find_alpha_beta(0, i, 1, j)
                print(alpha, beta)
                found = substitute_text(text, alpha, beta)
                print(found)
                print("\n\n")
            except:
                pass"""

    
    """
    alpha, beta = find_alpha_beta(25, 11, 11, 0)
    print(alpha, beta)
    found = substitute_text(text, alpha, beta)
    print(found)"""




    
