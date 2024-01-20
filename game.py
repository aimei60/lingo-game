import random
from words_file import words

def get_valid_word():
    word = random.choice(words)
    return word.lower()

print(get_valid_word())