import os
import random

#import a world list file named 'word.txt' or use the premade list

word_list = ['APPLE', 'BEACH', 'CROWD', 'DINGO', 'EATEN', 'FEAST', 'GRAPE', 'HEART', 'ITALY', 'JOLLY', 'KAYAK', 'KNIFE', 'LEMON', 'MANGO', 'NOTED', 'OPINE', 'PARTY','QUEUE', 'RATED', 'SHAME', 'TOUCH', 'UNCLE', 'VOICE', 'WATCH', 'XENON', 'YACHT','ZEBRA']


def hangman():
    word = random.choice(word_list).upper()
    attempts = 6

    print('Welcome to Python Hangman')
    print(f'Guess a {len(word)} letter word')
    guess_word = ['_'] * len(word)
    guessed_letters = []

    while attempts > 0:
        print('\nCurrent word: ' + ''.join(guess_word))
        if len(guessed_letters) > 0:
            print(f'Incorrect letters: {guessed_letters}')
        guess = input('Guess a letter: ').upper().strip()

        #check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.\n')
            continue

        #check if already guessed letter
        if (guess in guessed_letters) or (guess in guess_word):
            print('You already guessed that letter')
            continue        

        #check if guess is correct
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guess_word[i] = guess
                    print('Good Guess!\n')
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f'Wrong Guess. {attempts} attempts left.\n')

        #check if word is complete or if attempts have run out
        if '_' not in guess_word:
            print(f'Congratulations! You guessed the word {word}\n')
            break
        elif attempts == 0:
            print(f'Sorry you lose! The word was: {word}\n')

hangman()            