#computer picks a random word and prints _ _ _ _
#computer asks user to enter their guess
#there will be 5 attempts 
#user enters what they think the word is
#print what user guesses
#print if it matches to the correct word or not:
#if the letter is guessed in the right place, the letter will appear e.g. S _ _ _
#if the letter is guessed incorrectly, print incorrect letters on the side e.g s _ _ _ incorrect letters: e
#if the letter is guessed correctly but the letters are in the incorrect place, it will say so e.g. S _ _ _ correct letter but wrong place: l
#if user guesses before 5 attempts, user wins, guessed letter is solo
#if user doesn't guess and the attempts run out, user loses, print correct word: solo


import random
from words_file import words

def get_valid_word(word):
    word = random.choice(words)
    return word.upper()

def game():
    lives = 6
    word = get_valid_word(word)
    
