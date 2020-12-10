import random
from words import words
import string

def get_correct_word(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_correct_word(words)
    letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    lives = 8

    #game loop
    while len(letters) > 0 and lives > 0:
        print("You've got ", lives, "lives left")
        print("You've used these letters: ", ' '.join(used_letters))

        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        # word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current word is: ', ' '.join(word_list))
        
        input_letter = input('Guess a letter: ').upper()
        if input_letter in alphabet - used_letters:
            used_letters.add(input_letter)
            if input_letter in letters:
                letters.remove(input_letter)
                print(' ')
            else:
                lives -= 1
                print('\n "', input_letter, '" is not in the word')
        elif input_letter in used_letters:
            print("You've already used that letter, try another one")
        else:
            print("That's not a valid letter.")

    if lives == 0:
        print("You're hung! The word was ", word)
    else:
        print("Yeah, bitch! ", word, '!')


hangman()