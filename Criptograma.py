
#Function to count the number of letters in a text
def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    print(letters)
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

def caesar_cipher(text, n):
    new_text = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(text)):
        if text[i].isalpha():
            index = alphabet.index(text[i])
            new_index = (index + n) % 26
            new_text.append(alphabet[new_index])
        else:
            new_text.append(text[i])
            
    return "".join(new_text)

def caesar_decipher(text, n):
    return caesar_cipher(text, -n)
    

if __name__ == "__main__":
    
    with open("criptograma_1.txt", "r") as file:
        criptograma = file.read()
    
    #print(criptograma)
    
    freq_ordered_letters_1 = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'd', 'l', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'y', 'v', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']
    freq_ordered_letters_2 = ['a', 's', 'e', 'o', 'i', 'n', 'r', 'l', 'c', 't', 'd', 'u', 'm', 'p', 'b', 'g', 'h', 'v', 'q', 'y', 'f', 'z', 'j', 'x', 'k', 'w']

    print(sustitute_text(criptograma.lower(), freq_ordered_letters_2))
    
#print(caesar_decipher(criptograma.lower(), 25))