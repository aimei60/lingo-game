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
    return word.lower()

def display_word(word, used_letters):
    return " ".join([letter if letter in used_letters else '-' for letter in word])

def game():
    lives = 5
    word = get_valid_word(words)
    used_letters = set()
    incorrect_letters = []
    misplaced_letters = []

    print("word", display_word(word, used_letters))

    while lives > 0:
        user_word = input("Lives remaining: {}. Enter a word: ".format(lives)).lower()
        
        for user_char, comp_char in zip(user_word, word):
            if user_char == comp_char:
                used_letters.add(user_char)
            elif user_char in word and user_char not in misplaced_letters:
                misplaced_letters.append(user_char)
            elif user_char not in word and user_char not in incorrect_letters:
                incorrect_letters.append(user_char)

        feedback_word = display_word(word, used_letters)

        print("Feedback {}".format(feedback_word))
        if incorrect_letters:
            print("Incorrect letters: {}".format(' '.join(incorrect_letters)))
        if misplaced_letters:
            print("Correct letters in wrong place: {}".format(' '.join(misplaced_letters)))

        if user_word == word:
            print("Congratulations you guessed the word: {}".format(word))
            break
        
        lives -= 1
    
    if lives <= 0:
        print("Sorry you're out of lives. The word is {}".format(word))
        
if __name__ == "__main__":
    game()

