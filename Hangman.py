import random

word_list = []
#import a word list file or use the premade list. Make sure each word is in a new line
try:
    with open('word.txt', 'r') as f:
        for line in f:
            word_list.append(line.strip())
except FileNotFoundError:
    word_list = ['APPLE', 'BEACH', 'CROWD', 'DINGO', 'EATEN', 'FEAST', 'GRAPE', 'HEART', 'ITALY', 'JOLLY', 'KAYAK', 'KNIFE', 'LEMON', 'MANGO', 'NOTED', 'OPINE', 'OLIVE', 'PARTY','QUEUE', 'RATED', 'SHAME', 'TOUCH', 'UNCLE', 'VOICE', 'WATCH', 'XENON', 'YACHT','ZEBRA']


def hangman():
    word = random.choice(word_list).upper()
    attempts = 6

    print('Welcome to Python Hangman')
    print(f'Guess a {len(word)} letter word')
    guess_word = ['_'] * len(word)
    guessed_letters = []

    while attempts > 0:
        print('Current word: ' + ''.join(guess_word))
        if len(guessed_letters) > 0:
            print('Incorrect letters: ' + ''.join(guessed_letters) +'\n')
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
            print('Good Guess!')
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f'\nWrong Guess. {attempts} attempts left.')

        #check if word is complete or if attempts have run out
        if '_' not in guess_word:
            print(f'Congratulations! You guessed the word {word}\n')
            break
        elif attempts == 0:
            print(f'Sorry you lose! The word was: {word}\n')

if __name__ == '__main__':
    hangman()