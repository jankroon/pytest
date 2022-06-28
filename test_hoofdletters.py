# Unit tests voor hoofdletters.py spellingscorrectie
# Copyleft 2022: Hossein Chamani & Jan Kroon, Rotterdam University of Applied Sciences

import pytest
from hoofdletters import correct

# Unit Tests

def test_single_character():
    assert correct("a")== "A"

def test_space():
    assert correct(" ") == " "

def test_empty_string():
    assert correct("") == ""

def test_one_sentence():
    assert correct("vandaag is het maandag.") == "Vandaag is het maandag"

def test_two_sentences():
    assert correct("het is mooi weer. iedereen is vrolijk!") == "Het is mooi weer. Iedereen is vrolijk!"

