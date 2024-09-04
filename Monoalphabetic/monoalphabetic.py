
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
    text = re.sub(r"[^a-zñáéíóú]", "", text)
    #print(text)
    
    # Remove the accents
    text = remove_accents(text)
    return text

#############################################
    

if __name__ == "__main__":

    BLUE = '\033[94m'
    END = '\033[0m'
    
    with open("Criptograma3.txt", "r") as file:
        criptograma = file.read()
    
    text = clean_text(criptograma)
    print("Text:\n", text, "\n")
    #print(sort_letters(text))
    
    freq_ordered_letters_ = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'd', 'l', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']
    freq_ordered_letters_1 = ['e', BLUE+'a'+END , 'o', 's', 'r', 'n', 'i', 'd', BLUE+'l'+END, 'c', 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']

    #    freq_ordered_letters_1 = ['o', BLUE+'a'+END , 'n', BLUE+'e'+END, 'r', 's', 'i', 'c', BLUE+'l'+END, BLUE+'d'+END, 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']
    #freq_ordered_letters_1 = ['e', 'o', 'n', 'a', 'r', 's', 'i', 'd', 'l', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']

    #freq_ordered_letters_2 = ['a', 's', 'e', 'o', 'i', 'n', 'r', 'l', 'c', 't', 'd', 'm', 'u', 'p', 'y', 'v', 'h', 'f', 'b', 'g', 'q', 'z', 'j', 'x', 'k', 'w']

    print(sustitute_text(text.lower(), freq_ordered_letters_1))

    """repeated = repeated_substrings(text)
    for key in repeated:
        print(key, repeated[key][0])"""


    
