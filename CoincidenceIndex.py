import re

def clean_text(text):
    # Remove all punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove the scores and underscores
    text = re.sub(r'[-_]', '', text)
    # Remove all digits
    text = re.sub(r'\d', '', text)
    # Remove all extra spaces
    text = re.sub(r'\s+', '', text)
    # Convert to lowercase
    text = text.lower()
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
    for char in freq:
        count += dict_[char] * (dict_[char] - 1)
    count /= n * (n - 1)
    return index

"""# Test the function
text = "Hello, World!"
print(coincidence_index(text))  # 0.1111111111111111
text = "The quick brown fox jumps over the lazy dog."
print(coincidence_index(text))  # 0.05555555555555555"""

if __name__ == "__main__":
    
    print(clean_text("Hello, World!"))