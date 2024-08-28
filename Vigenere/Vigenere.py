import re

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

    repeated_substrings ={k: v for k, v in dict_.items() if v[0] > 1 and len(k) > 2}
    # Sort the dictionary by the length of the substring
    repeated_substrings = dict(sorted(repeated_substrings.items(), key=lambda item: len(item[0]), reverse=True))
    return repeated_substrings

# Function to find the difference between the positions of the repeated substrings
def kasiski_test(text):
    # Find the repeated substrings
    repeated = repeated_substrings(text)
    # Find the difference between the positions of the repeated substrings
    distances = {}
    for substring in repeated:
        positions = repeated[substring][1]
        for i in range(len(positions)-1): # Iterate over the positions of the substring
            diff = positions[i+1] - positions[i]
            if diff in distances:
                distances[diff] += 1
            else:
                distances[diff] = 1
    return dict(sorted(distances.items(), key=lambda item: item[1], reverse=True))

# Function to find the prime factors of a number
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n: # Iterate until the square root of n
        if n % i: # If n is divisible by i
            i += 1
        else:
            n //= i # Divide n by i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Function to find the factors of the distances
def factors(distances):
    factors = {}
    for distance in distances:
        factors[distance] = prime_factors(distance)
    return factors

# Function to show the factors of the distances
def find_key_length(factors):
    for factor in factors:
        print(f"Factor: {factor}")
        print(f"Prime factors: {factors[factor]}")
        print()
    
# Function to separate the text into n parts, letters separated by the key length
def separate_text(text, key_length):
    separated_text = []
    for i in range(key_length):
        separated_text.append(text[i::key_length]) # Append the characters separated by the key length
    return separated_text


#Function to count the number of letters in a text
def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

# Function to sort the letters by the number of times they appear
def sort_letters(text):
    counts = count_letters(text)
    def get_count(letter):
        return counts[letter]
    return sorted(counts.keys(), key=get_count, reverse=True)

def get_sorted_letters_of_every_alphabet(separated_text):
    sorted_letters = []
    for alphabet in separated_text:
        sorted_letters.append(sort_letters(alphabet))
    return sorted_letters

# Get the key letter if we have the vigenere encrypted letter and the proposed actual letter
def get_key_letter(vigenere_letter, actual_letter):
    #freq_ordered_letters = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'd', 'l', 't', 'u', 'c', 'm', 'p', 'v', 'g', 'b', 'q', 'f', 'h', 'z', 'j', 'x', 'y', 'k', 'w']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vigenere_index = alphabet.index(vigenere_letter) # Index of the vigenere letter
    actual_index = alphabet.index(actual_letter) # Index of the actual letter
    key_index = (vigenere_index - actual_index) % 26 # Index of the key letter
    return alphabet[key_index]

def get_key(sorted_letters):
    key = []
    for i in range(len(sorted_letters)):
        key.append(get_key_letter(sorted_letters[i][0], "a"))
    return key



def vigenere_table():
    table = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table



if __name__ == "__main__":
    # Read the text from the file
    with open("criptograma_2.txt", "r", encoding='latin-1') as file:
        text = file.read()

    text = clean_text(text)
    #print(coincidence_index(text))
    #distances = kasiski_test(text)
    #print(factors(distances))
    #print(find_key_length(factors(distances)))
    separated_text = separate_text(text, 10)
    #print(separated_text)
    sorted_alphabets_letters= get_sorted_letters_of_every_alphabet(separated_text)
    #print(sorted_alphabets_letters)
    print(get_key(sorted_alphabets_letters))
    