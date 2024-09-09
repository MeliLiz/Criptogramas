
import re

# Find the gcd of two numbers
def gcd(a, b):  
    if b == 0:  
        return a  
    else:  
        return gcd(b, a % b)


# Find the possible texts that can be decrypted
def find_possible_texts(text):
    possible_a = [x for x in range(26) if gcd(x, 26)==1] # List of possible values for a, values that have inverse modulo 26
    for b in range(26):
        for a in possible_a:
            decripted = decrypt(text, a, b)
            print(f"a = {a}, b = {b}: {decripted} \n")

def decrypt(text, a, b):
    new = []
    a_inverse = [x for x in range(26) if (a * x) % 26 == 1][0] # Find the inverse of a modulo 26
    for letter in text:
        letter = ord(letter) - 97
        new.append(chr(((a*(letter-b)) % 26 ) + 97))
    return "".join(new)




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
    

if __name__ == "__main__":

  
    
    with open("Criptograma3.txt", "r") as file:
        criptograma = file.read()
    
    text = clean_text(criptograma)
    # print(text)
    find_possible_texts(text)
   
