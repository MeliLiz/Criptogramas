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

# Function to find the separation betweeen the repeated substrings
"""def kasiski_test(text):
    repeated_subs = repeated_substrings(text)
    # Find the separation between the repeated substrings
    distances = {}
    for substring in repeated_subs:
        positions = [m.start() for m in re.finditer(f"(?={re.escape(substring)})", text)]
        
        if len(positions) > 1:
            substring_distances = []
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[i]
                substring_distances.append(distance)
            distances[substring] = substring_distances

    # Step 3: Find the greatest common divisor (GCD) of all distances
    gcds = []
    for substring, dist_list in distances.items():
        if len(dist_list) > 1:
            gcds.append(reduce(gcd, dist_list))

    # Step 4: Determine possible key lengths by looking at the most common GCDs
    possible_key_lengths = list(set(gcds))
    possible_key_lengths.sort()
    
    return possible_key_lengths, distances"""
    


if __name__ == "__main__":
    # Read the text from the file
    with open("criptograma_2.txt", "r", encoding='latin-1') as file:
        text = file.read()

    #print(coincidence_index(text))
    print(repeated_substrings(text))
    #print(kasiski_test(text))
