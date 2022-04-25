import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    numLetters = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            numLetters += 1
    return numLetters == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    soFar = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            soFar = soFar + letter + ' '
        else:
            soFar = soFar + '_ '
    return soFar


def getAvailableLetters(lettersGuessed):
    import string
    engLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        engLetters.remove(letter)
    return ''.join(engLetters)


def hangman(secretWord):
    def pleaseGuess(guesses, AtoZ):
        print('-'*11)
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + AtoZ)
        letter = input('Please guess a letter: ')
        return letter

    # start of game:
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long')
    guesses = 8
    lettersGuessed = []

    # rounds:
    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        letter = pleaseGuess(guesses, getAvailableLetters(lettersGuessed))
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                  getGuessedWord(secretWord, lettersGuessed))
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            guesses -= 1
            lettersGuessed.append(letter)
            print("Oops! That letter is not in my word: " +
                  getGuessedWord(secretWord, lettersGuessed))
    # win or lose:
    print('-'*11)
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
