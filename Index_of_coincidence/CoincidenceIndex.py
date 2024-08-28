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


if __name__ == "__main__":
    # Read the text from the file
    with open("texto.txt", "r", encoding='latin-1') as file:
        text = file.read()

    print(coincidence_index(text))
