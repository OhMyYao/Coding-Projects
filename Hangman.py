import random

word_list = ['APPLE', 'BEACH', 'CROWD', 'DINGO', 'EATEN', 'FEAST', 'GRAPE', 'HEART']

def wordle():
    select_word = random.choice(word_list).upper()
    attempts = 6

    print('Welcome to Python Wordle')
    print('Guess a 5 letter word')

    while attempts > 0:
        
        attempts -= 1