
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
def sort_letters(letters):
    def get_count(letter):
        return letter[1]
    return sorted(letters.items(), key=get_count, reverse=True)

def get_sustitutions(criptograma, freq_ordered_letters):
    letters = sort_letters(count_letters(criptograma))
    sustitutions = {}
    for i in range(len(letters)):
        sustitutions[letters[i]] = freq_ordered_letters[i]
    return sustitutions

# Function to sustitute the letters in the text
# sustitutions is a dictionary with the letters to be sustituted
def sustitute_text(text, sustitutions):
    new_text = []
    for letter in text:
        if letter.isalpha():
            new_text.append(sustitutions[letter[0]])
        else:
            new_text.append(letter)
    return "".join(new_text)

if __name__ == "__main__":
    with open("criptograma_1.txt", "r") as file:
        criptograma = file.read()
        
    freq_ordered_letters = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'd', 'l', 't', 'u', 'c', 'm', 'p', 'v', 'g', 'b', 'q', 'f', 'h', 'j', 'z', 'x', 'y', 'k', 'w']
    sustitutions = get_sustitutions(criptograma.lower(), freq_ordered_letters)
    print(sustitutions)
    print(sustitute_text(criptograma, sustitutions))
    
        