import re
from itertools import permutations

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



def obtener_permutaciones(cadena):
    permus = permutations(cadena)
    cont = 0
    for p in permus:
        # if n is in the same column or row as l and o, l should be at the left of n or at the top of n and o should be at the left of l or at the top of l
        ind_n = p.index("n")
        col_n = ind_n % 5
        row_n = ind_n // 5
        ind_l = p.index("l")
        col_l = ind_l % 5
        row_l = ind_l // 5
        ind_o = p.index("o")
        col_o = ind_o % 5
        row_o = ind_o // 5
        # Should be o l n
        if col_n == col_l and col_l == col_o: # o, l n are in the same column
            if row_o == row_l - 1 % 5 and row_l == row_n - 1 % 5:
                #print(p)
                cont += 1
            else:
                continue
        elif row_n == row_l and row_l == row_o: # o, l n are in the same row
            if col_o == col_l - 1 % 5 and col_l == col_n - 1 % 5:
                #print(p)
                cont += 1
        else:   # cannot be forming a square
            continue

    print(cont)
        

# Ejemplo de uso
cadena = "abcdefghijklmnopqrstuvxyz"
permutaciones = obtener_permutaciones(cadena)
#print(permutaciones)



# Bleak playfair cipher
def break_playfair(text):
    #Get th possible keys
    alphabet = "abcdefghijklmnopqrstuvxyz" # not including the letter 'w'
    keys = []
    for i in range(25):
        print(i)

if __name__ == "__main__":
    with open("Criptograma6.txt", "r") as file:
        criptograma = file.read()

    text = clean_text(criptograma)
