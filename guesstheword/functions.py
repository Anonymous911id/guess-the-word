import random
from guesstheword.wordslist import words

def get_word():
    word = random.choice(words)
    # if '-' or ' ' between words, the code below is also needed
    # while '-' in word or ' ' in word:
        # word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letters = ''
    for letter in word:
        if letter in user_letters:
            display_letters += letter
        else:
            display_letters += '-'
    return display_letters

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ''
    print(f"I thought of {len(word)} digit word")

    while len(word_letters) > 0:
        print(display(user_letters, word))  
        if len(user_letters) > 0:
            print(f"The letters you have entered until now: {user_letters}")

        letter = input("Enter a letter: ").upper()
        if letter in user_letters:
            print("You have already entered this letter. Enter another letter.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"The letter {letter} is correct")
        else:
            print("There is no such letter")
        user_letters += letter
    print(f"Congratulations! you have found the word '{word}' in {len(user_letters)} tries")