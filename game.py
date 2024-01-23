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

def get_valid_word(words):
    word = random.choice(words)
    return word.upper()

def game():
    lives = 6
    word = get_valid_word(words)
    used_letters = set()
    incorrect_letters = ""
    misplaced_letters = ""

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Word: ", " ".join(word_list))

    user_word = input("Enter a word: ").upper()
    #need to break the word into letters to assess it/ compare later down the line function 
    print(user_word)
    
# need to compare the user letter to the computer letter in their words respectively
    # for any of the positions in the in the word 
    #if the user letter and the computer letter matches:
        #reveal the letter and the rest of the unguessed word e.g. S - - -
    #if the user letter is in the computer word but in the wrong place:
        #append user letter to misplaced_letters
        #print misplaced_letters and the computer word so far
        #lives -= 1
    # if the letter is not in the computer word:
        #append the letter to incorrect_letters
        #print incorrect_letters and the computer word so far
        #lives -= 1
    
#need to add the lives 
#need to add how the game concludes, user guessed within 5 lives and wins or loses and the word is revealed
    
    
    for letter in word:
        
        
    

game()

