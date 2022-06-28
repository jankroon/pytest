# Spellings-correctie software. Zet voorlopig alleen hoofdletters aan het begin van een zin
# CopyLeft 2022, Jan Kroon (Rotterdam University of Applied Sciences)

# ASCII code of <space> is 32
# ASCII code of <dot> is 46

import pytest

# User Interface

print("*** Spellingscorrectie ***")
print()
text = input("Type hier uw tekst, met interpunctie: ")

# Spelling correction 

def correct(check_text):
    correct_text = ""
    capitalize_next_letter = True
    
    for token in check_text:
        if capitalize_next_letter and ord(token) != 32:
#           print(token.upper(), end="")
            correct_text = correct_text + token.upper()
            capitalize_next_letter = False
        else:
#           print(token, end="")
            correct_text = correct_text + token
        if ord(token) == 46:
            capitalize_next_letter = True
    return correct_text

print(correct(text))

