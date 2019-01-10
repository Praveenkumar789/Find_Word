# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

'''You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter:")'''



def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=0
    for letter in secretWord:
        if letter in lettersGuessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False
            
    
        
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    optstr=[]
    for i in range(len(secretWord)):
        optstr.extend(['_', ' '])
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            optstr[2*i]=secretWord[i]
    string=''
    for i in range(len(optstr)):
        string+=optstr[i]  
    return string

def getAvailableLetters(lettersGuessed):
    '''
    
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabets='abcdefghijklmnopqrstuvwxyz'
    Alphabets=''
    Alphas=list(alphabets)
    for letter in lettersGuessed:
        if letter in Alphas:
            Alphas.remove(letter)
    for letter in Alphas:
        Alphabets+=letter
    return Alphabets
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed=[]
    Guesses=8
    mistakesmade=0
    correct_guessed=[]
    wrong_guessed=[]
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print('-------------')
    print("you have ",Guesses-mistakesmade," guesses left")
    print("Available letters: "+getAvailableLetters(lettersGuessed))
    while True:
        char=input("please guess a letter:")
        lettersGuessed.append(char)
        if char in secretWord:
            if char not in correct_guessed:
                correct_guessed.append(char)
                print("Good Guess: "+getGuessedWord(secretWord, lettersGuessed)) 
                print('-------------')
            else:
                print("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
        else:
            if char not in wrong_guessed:
                wrong_guessed.append(char)
                mistakesmade+=1
                print("Oops! That letter is not in my word: _ ")
                print('-------------')
            else:
                print("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
        check=isWordGuessed(secretWord, lettersGuessed)
        if check==True:
            print("Congratulations you won!")
            break
        if mistakesmade==Guesses:
            print("Sorry, you ran out of guesses. The word was else.")
            break
        print("you have ",Guesses-mistakesmade," guesses left")
        print("Available letters: "+getAvailableLetters(lettersGuessed))
    print("Here's the word "+str(secretWord))
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
