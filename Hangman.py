import random

word_list = ['APPLE', 'BEACH', 'CROWD', 'DINGO', 'EATEN', 'FEAST', 'GRAPE', 'HEART']

def hangman():
    word = random.choice(word_list).upper()
    attempts = 6

    print('Welcome to Python Hangman')
    print('Guess a 5 letter word')
    guess_word = ['_'] * len(word)

    while attempts > 0:
        print('\nCurrent word: ' + ''.join(guess_word))
        guess = input('Guess a letter: ').upper()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guess_word[i] == guess
                    print('Good Guess!\n')
                else:
                    attempts -= 1
                    print(f'Wrong Guess. {str(attempts)} attempts left.\n')

        if '_' not in guess_word:
            print(f'Congratulations! You guessed the word {word}\n')
            break
        elif attempts == 0:
            print(f'Sorry you lose! The word was: {word}\n')

hangman()            