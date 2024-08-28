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

def factors(distances):
    factors = {}
    for distance in distances:
        factors[distance] = prime_factors(distance)
    return factors
    


if __name__ == "__main__":
    # Read the text from the file
    with open("criptograma_2.txt", "r", encoding='latin-1') as file:
        text = file.read()

    #print(coincidence_index(text))
    #print(repeated_substrings(text))
    distances = kasiski_test(text)
    print(factors(distances))
